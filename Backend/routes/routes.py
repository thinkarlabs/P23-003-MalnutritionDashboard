from Backend.model.model import AaganwadiSummary
from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from Backend.model.model import ProgramJoining
from Backend.config.database import AanganwadiCollection
from Backend.config.database import ProgramsCollection, ProgramJoiningCollection, AangawadiSummaryCollection
from Backend.schemas.schema import program_list_serializer
from Backend.schemas.schema import programjoining_list_serializer
from typing import Union


child_malnutrition = APIRouter()
program_joining = APIRouter()
aaganwadi_summary = APIRouter()


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
