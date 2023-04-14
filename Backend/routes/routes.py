from Backend.model.model import AaganwadiSummary
from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from Backend.model.model import ChildMalnutrition, ProgramJoining
from Backend.config.database import AanganwadiCollection, ChildCollection
from Backend.config.database import ChildMalnutritionCollection,  \
    ProgramsCollection, ProgramJoiningCollection, AangawadiSummaryCollection
from Backend.schemas.schema import program_list_serializer
from Backend.schemas.schema import child_malnutrition_list_serializer, programjoining_list_serializer
from typing import Union


child_malnutrition = APIRouter()
program_joining = APIRouter()
aaganwadi_summary = APIRouter()


@child_malnutrition.post("/api/childMalnutrion_Add")
async def child_malnutrition_add(child: ChildMalnutrition):
    """
    This function is created for add the child malnutrition details basis on child id.
    :param child: A Pydantic model representing ChildMalnutrition data to be created.
    :return: Response status and newly created ChildMalnutrition data.
    """
    if not ChildCollection.find_one({"_id": ObjectId(child.child_id)}):
        raise HTTPException(status_code=404, detail="Child not found")
    _id = ChildMalnutritionCollection.insert_one(dict(child))
    added_malnutrition_child = child_malnutrition_list_serializer(ChildMalnutritionCollection.find(
        {"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_malnutrition_child}


@child_malnutrition.get("/api/get_child_Malnutritions")
async def get_child_malnutritions():
    """
    This function is created for retrieve all child malnutrition data from db.
    :return: Response status and fetched data from db.
    """
    childs = child_malnutrition_list_serializer(
        ChildMalnutritionCollection.find())
    return {"status": "ok", "data": childs}


@child_malnutrition.get("/api/{child_id}/get_child_malnutrition_stats")
async def get_child_malnutrition_stats(child_id: str):
    """
    This function is create for get the particular child malnutrition data.
    :param id: id of the ChildMalnutrition to retrieve.
    :return: Response status and fetched particular data.
    """
    child = child_malnutrition_list_serializer(
        ChildMalnutritionCollection.find({"child_id": str(child_id)}))
    print(child)
    return {"status": "ok", "data": child}


@child_malnutrition.put("/api/update_child_malnutrition")
async def update_child_malnutrition(id: str, childs: ChildMalnutrition):
    """
    This function is create for update the child malnutrition details.
    :param id: id of the ChildMalnutrition to be updated.
    :param childs: The pydantic model representing the updated ChildMalnutrition data.
    :return: Response status and updated ChildMalnutrition data.
    """
    ChildMalnutritionCollection.find_one_and_update({"_id": ObjectId(id)},
                                                    {"$set": dict(childs)})
    updated_value = child_malnutrition_list_serializer(
        ChildMalnutritionCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_value}


@child_malnutrition.delete("/deleteChild_malnutrition")
async def delete_child(id: str):
    """
    This function is create for delete the child malnutrition details.
    :param id: id of the ChildMalnutrition to be deleted
    :return: Response status
    """
    ChildMalnutritionCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@program_joining.post("/api/Add_program_joining")
async def add_program_joining(programs: ProgramJoining):
    result = ProgramsCollection.find_one({"invite_code": programs.invite_code})
    identifedAaganwadi = AanganwadiCollection.find_one(
        {"_id": ObjectId(programs.aanganwadi_id)})
    if not result:
        raise HTTPException(status_code=404, detail="Invalid invite code")
    elif not identifedAaganwadi:
        raise HTTPException(status_code=404, detail="Invalid Aaganwadi")
    else:
        programs.program_id = str(result['_id'])
        _id = ProgramJoiningCollection.insert_one(dict(programs))
        add_joining_details = programjoining_list_serializer(
            ProgramJoiningCollection.find({"_id": _id.inserted_id}))
        return {"status": "ok", "data": add_joining_details}


@program_joining.get("/api/get_programs_joining_details")
async def get_programs():
    programs = programjoining_list_serializer(
        ProgramJoiningCollection.find())
    return {"status": "ok", "data": programs}


@program_joining.get("/api/get_program_joining_details/{aanganwadi_id}")
async def get_program_joining_details(aanganwadi_id: str):

    list_of_program_joining_summary = []
    program_joining_array = programjoining_list_serializer(
        ProgramJoiningCollection.find({"aanganwadi_id": str(aanganwadi_id)}))
    print(program_joining_array)
    for program_joining_obj in program_joining_array:
        program_id = program_joining_obj["program_id"]
        program_joining_id = program_joining_obj["id"]
        program_details = program_list_serializer(
            ProgramsCollection.find({"_id": ObjectId(program_id)}))
        if len(program_details) > 0:
            donor_name = program_details[0]["donor_name"]
            supplement_name = program_details[0]["supplement_name"]
            from_date = program_details[0]["from_date"]
            to_date = program_details[0]["to_date"]
            program_joining_object = {
                "program_joining_id": program_joining_id,
                "donor_name": donor_name,
                "supplement_name": supplement_name,
                "from_date": from_date,
                "to_date": to_date
            }
            list_of_program_joining_summary.append(program_joining_object)
    return {"status": "ok", "data": list_of_program_joining_summary}


# FastAPI endpoint to retrieve the summary of an Aaganwadi program
@aaganwadi_summary.get("/aaganwadi/summary/{aaganwadi_id}")
async def get_aaganwadi_summary(aaganwadi_id: str):
    # Query the MongoDB database for the Aaganwadi program summary
    summary = AangawadiSummaryCollection.find_one({"_id": aaganwadi_id})

    # If summary is None, return 0 for all categories
    if summary is None:
        return AaganwadiSummary()

    # Calculate the change count compared to the last week
    sam_change = summary.get("SAMCountThisWeek", 0) - \
        summary.get("SAMCountLastWeek", 0)
    mam_change = summary.get("MAMCountThisWeek", 0) - \
        summary.get("MAMCountLastWeek", 0)
    normal_change = summary.get(
        "NormalCountThisWeek", 0) - summary.get("NormalCountLastWeek", 0)

    # Initialize a new instance of the AaganwadiSummary class with the summary data
    aaganwadi_summary = AaganwadiSummary(
        TotalChildCount=summary.get("TotalChildCount", 0),
        SAMCountThisWeek=summary.get("SAMCountThisWeek", 0),
        MAMCountThisWeek=summary.get("MAMCountThisWeek", 0),
        NormalCountThisWeek=summary.get("NormalCountThisWeek", 0),
        SAMChangeCount=sam_change,
        MAMChangeCount=mam_change,
        NormalChangeCount=normal_change
    )

    # Return the AaganwadiSummary instance as the response
    return aaganwadi_summary
