from Backend.model.model import AaganwadiSummary
from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from Backend.model.model import Ngo,User, ChildMalnutrition, Program, ProgramJoining
from Backend.config.database import UserCollection, AanganwadiCollection, ChildCollection, \
    SupplementDetailsCollection
from Backend.config.database import DonorsCollection, ChildMalnutritionCollection,  \
    ProgramsCollection, ProgramJoiningCollection, AangawadiSummaryCollection, NgoCollection
from Backend.schemas.schema import user_list_serializer, program_list_serializer
from Backend.schemas.schema import ngo_list_serializer, aanganwadi_list_serializer
from Backend.schemas.schema import child_malnutrition_list_serializer, programjoining_list_serializer
from typing import Union

user_router = APIRouter()
ngo_router = APIRouter()
child_malnutrition = APIRouter()
program_router = APIRouter()
program_joining = APIRouter()
aaganwadi_summary = APIRouter()


@user_router.post("/api/create_user")
async def create_user(user: User):
    _id = UserCollection.insert_one(dict(user))
    added_user = user_list_serializer(
        UserCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_user}


@user_router.get("/api/get_users")
async def get_users():
    users = user_list_serializer(UserCollection.find())
    return {"status": "ok", "data": users}


@user_router.get(f"/api/{id}/get_user")
async def get_user(id: str):
    user = user_list_serializer(UserCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": user}


def Validate_User_Object(username, password):
    valid = 0
    userSearched = user_list_serializer(UserCollection.find(
        {'username': str(username), 'password': str(password)}))
    ngoSearched = ngo_list_serializer(
        NgoCollection.find({"contactPersonName": str(username), "contactPersonPassword": str(password)}))
    aaganwadiSearched = aanganwadi_list_serializer(AanganwadiCollection.find(
        {'contactPersonName': str(username), 'contactPersonPassword': str(password)}))
    identifiedUser = User(username=str(username), password=str(
        password), user_type=str(""))
    if (ngoSearched):
        identifiedUser.user_type = "ngo"
    elif (aaganwadiSearched):
        identifiedUser.user_type = "aaganwadi"
    elif (userSearched):
        identifiedUser.user_type = "admin"
    print('identifiedUser' + str(identifiedUser))
    return identifiedUser


@user_router.post("/api/isvaliduser")
async def read_item(requestUser: User):
    identifiedUser = Validate_User_Object(
        requestUser.username, requestUser.password)
    if identifiedUser.user_type == "":
        raise HTTPException(
            status_code=404, detail="Invalid username or password")
        # return {"response": "Invalid username or password"}
    else:
        return {"status": "ok", "data": identifiedUser}
        # raise HTTPException(status_code=200, detail="Successful login")
        # return {"response":"Successful login"}


@program_router.post("/api/add_program")
async def add_program(program: Program):
    donor_details = DonorsCollection.find_one(
        {"_id": ObjectId(program.donor_id)})
    suplement_details = SupplementDetailsCollection.find_one(
        {"_id": ObjectId(program.supplements_details_id)})
    if not donor_details and suplement_details:
        raise HTTPException(status_code=404, detail="input are missing")
    program.donor_name = str(donor_details['name'])
    program.supplement_name = str(suplement_details['name'])
    _id = ProgramsCollection.insert_one(dict(program))
    added_programs = program_list_serializer(ProgramsCollection.find(
        {"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_programs}


@program_router.get("/api/get_programs")
async def get_programs():
    programs = program_list_serializer(
        ProgramsCollection.find())
    return {"status": "ok", "data": programs}


@program_router.get("/api/get_program/{id}")
async def get_program(id: str):
    result = program_list_serializer(
        ProgramsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": result}


@program_router.put("/api/update_program/{id}")
async def update_program(id: str, program: Program):
    ProgramsCollection.find_one_and_update({"_id": ObjectId(id)},
                                           {"$set": dict(program)})
    updated_value = program_list_serializer(
        ProgramsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_value}


@program_router.delete("/api/delete_program/{id}")
async def delete_program(id: str):
    ProgramsCollection.find_one_and_delete({"_id": ObjectId(id)})
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
