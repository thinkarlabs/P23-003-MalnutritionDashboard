from Backend.model.model import SupplementaryPacks, AaganwadiSummary
from Backend.config.database import SupplementaryCollection
from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from Backend.model.model import Ngo, User, Donor, Aanganwadi, Child, ChildMalnutrition, SupplementsDetail, Program, \
    ProgramJoining
from Backend.config.database import NgoCollection, UserCollection, AanganwadiCollection, ChildCollection
from Backend.config.database import DonorsCollection, ChildMalnutritionCollection, SupplementDetailsCollection, \
    ProgramsCollection, ProgramJoiningCollection, AangawadiSummaryCollection
from Backend.schemas.schema import ngo_list_serializer, user_list_serializer, donors_list_serializer, \
    program_list_serializer
from Backend.schemas.schema import supplements_list_serializer
from Backend.schemas.schema import aanganwadi_list_serializer, child_list_serializer, \
    child_malnutrition_list_serializer, programjoining_list_serializer, supplementaryPacks_list_serializer
from typing import Union

user_router = APIRouter()
ngo_router = APIRouter()
donor_router = APIRouter()
aanganwadi_router = APIRouter()
child_router = APIRouter()
child_malnutrition = APIRouter()
supplement_details = APIRouter()
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


def Validate_User_Object(email, password, user_type):
    valid = 0
    for user in UserCollection.find():
        if (user['username'] == email) & (user['password'] == password) & (user['user_type'] == user_type):
            valid = 1
    return valid


@user_router.get("/api/isvaliduser")
async def read_item(username: str, password: Union[str, None] = None, user_type: Union[str, None] = None):
    valid = Validate_User_Object(username, password, user_type)
    if valid == 0:
        raise HTTPException(status_code=404, detail="user not found")
        # return {"response":"Invalid username or password"}
    else:
        raise HTTPException(status_code=200, detail="Successful login")
        # return {"response":"Successful login"}


@ngo_router.post("/api/create_ngo")
async def create_ngo(ngo: Ngo):
    _id = NgoCollection.insert_one(dict(ngo))
    added_ngo = ngo_list_serializer(
        NgoCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_ngo}


@ngo_router.get("/api/getNgos")
async def get_ngos():
    ngos = ngo_list_serializer(NgoCollection.find())
    return {"status": "ok", "data": ngos}


@ngo_router.get("/api/{id}/get_ngo")
async def get_ngo(id: str):
    ngo = ngo_list_serializer(
        NgoCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": ngo}


@ngo_router.put("/ngos/{ngo_id}")
async def update_ngo(id: str, ngo: Ngo):
    NgoCollection.find_one_and_update({"_id": ObjectId(id)},
                                      {"$set": dict(ngo)})
    updated_value = ngo_list_serializer(
        NgoCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_value}


@ngo_router.delete("/api/delete_ngo/{id}")
async def delete_ngo(id: str):
    NgoCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@donor_router.post("/api/donors")
async def create_donor(donor: Donor):
    _id = DonorsCollection.insert_one(dict(donor))
    donor = donors_list_serializer(
        DonorsCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": donor}


@donor_router.get("/api/getdonors")
async def get_donors():
    donors = donors_list_serializer(DonorsCollection.find())
    return {"status": "ok", "data": donors}


@donor_router.get("/api/{id}/get_donor")
async def get_donor(id: str):
    donor = donors_list_serializer(
        DonorsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": donor}


@donor_router.delete("/api/delete_donor/{id}")
async def delete_donor(id: str):
    DonorsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@donor_router.put("/api/donors/{id}")
async def update_donor(id: str, donor: Donor):
    DonorsCollection.find_one_and_update({"_id": ObjectId(id)},
                                         {"$set": dict(donor)})
    updated_data = donors_list_serializer(
        DonorsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_data}


@aanganwadi_router.post("/api/addAanganwadi")
async def aanganwadi_addition(aanganwadi: Aanganwadi):
    _id = AanganwadiCollection.insert_one(dict(aanganwadi))
    added_aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_aanganwadi}


@aanganwadi_router.get("/api/getAanganwadis")
async def get_aanganwadis():
    aanganwadis = aanganwadi_list_serializer(AanganwadiCollection.find())
    return {"status": "ok", "data": aanganwadis}


@aanganwadi_router.get("/api/{id}/get_aanganwadi")
async def get_aanganwadi(id: str):
    aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": aanganwadi}


@aanganwadi_router.put("/api/updateAanganwadi/{id}")
async def update_aanganwadi(id: str, aanganwadi: Aanganwadi):
    AanganwadiCollection.find_one_and_update({"_id": ObjectId(id)},
                                             {"$set": dict(aanganwadi)})
    aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": aanganwadi}


@aanganwadi_router.delete("/api/delete_aanganwadi/{id}")
async def delete_aanganwadi(id: str):
    AanganwadiCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@child_router.post("/api/add_child")
async def add_child(child: Child):
    _id = ChildCollection.insert_one(dict(child))
    added_child = child_list_serializer(
        ChildCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_child}


@child_router.get("/api/get_childs")
async def get_childs():
    childs = child_list_serializer(ChildCollection.find())
    return {"status": "ok", "data": childs}


@child_router.get("/api/{id}/get_child")
async def get_child(id: str):
    childs = child_list_serializer(
        ChildCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": childs}


@child_router.put("/api/updatechild/{id}")
async def update_child(id: str, child: Child):
    ChildCollection.find_one_and_update({"_id": ObjectId(id)},
                                        {"$set": dict(child)})
    updated_child = child_list_serializer(
        ChildCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_child}


@child_router.delete("/api/deletechild")
async def delete_child(id: str):
    ChildCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


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


supp_router = APIRouter()


# Create Supplementary pack detail


@supp_router.post('/api/add_supplement_pack/')
async def add_supplement_pack(supplementary: SupplementaryPacks):
    print(supplementary)
    _id = SupplementaryCollection.insert_one(dict(supplementary))
    add_supplementary = supplementaryPacks_list_serializer(
        SupplementaryCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": add_supplementary}


# Read all Supplementary pack details of a given program joining id

@supp_router.get('/api/get_all_supplemet_packs/{program_joining_id}')
async def get_all_supplemet_packs_for_a_program(program_joining_id: str):
    supplementary = supplementaryPacks_list_serializer(
        SupplementaryCollection.find({"program_joining_id": str(program_joining_id)}))
    return {"status": "ok", "data": supplementary}


# Read a single Supplementary pack detail


@supp_router.get('/api/get_supplement_pack/{supplementary_id}')
async def get_supplement_pack(supplementary_id: str):
    supplementary = supplementaryPacks_list_serializer(
        SupplementaryCollection.find({"_id": ObjectId(supplementary_id)}))
    return {"status": "ok", "data": supplementary}


# Update a Supplementary pack detail

@supp_router.put('/api/update_supplement_pack/{supplementary_id}')
async def update_supplement_pack(supplementary_id: str, supplementary: SupplementaryPacks):
    SupplementaryCollection.find_one_and_update({"_id": ObjectId(supplementary_id)},
                                                {"$set": dict(supplementary)})
    updated_supplementary = supplementaryPacks_list_serializer(
        SupplementaryCollection.find({"_id": ObjectId(supplementary_id)}))
    return {"status": "ok", "data": updated_supplementary}


# Delete a Supplementary pack detail

@supp_router.delete('/api/delete_supplement_pack/{supplementary_id}')
def delete_supplement_pack(supplementary_id: str):
    result = SupplementaryCollection.find_one_and_delete(
        {"_id": ObjectId(supplementary_id)})
    return {"message": "supplementary deleted successfully"}


@supplement_details.post('/api/add_supplement_details')
def add_supplement_details(supplement: SupplementsDetail):
    """
    This function is create for add the supplement details.
    :param supplement: A Pydantic model representing the supplement data to be created.
    :return: Response status and newly created supplement data.
    """
    _id = SupplementDetailsCollection.insert_one(dict(supplement))
    added_supplement = supplements_list_serializer(
        SupplementDetailsCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_supplement}


@supplement_details.get('/api/get_supplements_details')
async def get_supplements_details():
    """
    This function is create for get the supplement details.
    :return: Response status and fetched all data from db
    """
    result = supplements_list_serializer(SupplementDetailsCollection.find())
    return {"status": "ok", "data": result}


@supplement_details.get('/api/{id}/get_supplement_details')
async def get_supplement_details(id: str):
    """
    This function is create to retrieve particular supplement details.
    :param id: id of the supplements to retrieve.
    :return: Response status and a dictionary representing the supplement data in a custom format.
    """
    result = supplements_list_serializer(
        SupplementDetailsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": result}


@supplement_details.put('/api/update_supplement_details/{id}')
async def update_supplement_details(id: str, supplement: SupplementsDetail):
    """
    This function is create to update the supplement details.
    :param id: id of the supplement to be updated.
    :param supplement: The pydantic model representing the updated supplement data.
    :return: Response status and updated supplement data.
    """
    SupplementDetailsCollection.find_one_and_update({"_id": ObjectId(id)},
                                                    {"$set": dict(supplement)})
    updated_value = supplements_list_serializer(
        SupplementDetailsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_value}


@supplement_details.delete('/api/delete_supplement_details/{id}')
async def delete_supplement_details(id: str):
    """
    This function is create to delete the supplement details.
    :param id: id of the supplement to be deleted.
    :return: Response status.
    """
    SupplementDetailsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


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
