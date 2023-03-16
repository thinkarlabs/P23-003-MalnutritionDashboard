from Backend.model.model import Supplementary, Program
from Backend.config.database import SupplementaryCollection, ProgramsCollection
from typing import List
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from argparse import OPTIONAL
from fastapi import APIRouter, Body
from Backend.model.model import Ngo, User, Donor, Aanganwadi, Child, ChildMalnutrition, SupplementsDetail, Program
from Backend.config.database import NgoCollection, UserCollection, AanganwadiCollection, ChildCollection
from Backend.config.database import DonorsCollection, ChildMalnutritionCollection, SupplementDetailsCollection, \
    ProgramsCollection
from Backend.schemas.schema import ngo_list_serializer, user_list_serializer, donors_list_serializer
from Backend.schemas.schema import supplements_list_serializer
from Backend.schemas.schema import aanganwadi_list_serializer, child_list_serializer, child_malnutrition_list_serializer
from typing import Union

user_router = APIRouter()
ngo_router = APIRouter()
donor_router = APIRouter()
aanganwadi_router = APIRouter()
child_router = APIRouter()
child_malnutrition = APIRouter()
supplement_details = APIRouter()
program_router = APIRouter()
program_router = APIRouter()


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
        DonorsCollection.find({"id": _id.inserted_id}))
    return {"status": "ok", "data": donor}


@donor_router.get("/api/getdonors")
async def get_donors():
    donors = donors_list_serializer(DonorsCollection.find())
    return {"status": "ok", "data": donors}


@donor_router.get(f"/api/{id}/get_donor")
async def get_donor(id: str):
    donor = donors_list_serializer(
        DonorsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": donor}


@donor_router.delete("/api/delete_donor/{id}")
async def delete_donor(id: str):
    DonorsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@donor_router.put("/api/donors/{donor_id}")
async def update_donor(donor_id: str, donor: Donor):
    result = DonorsCollection.update_one(
        {"_id": donor_id}, {"$set": donor.dict()})
    return {"updated": result.modified_count}


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


@aanganwadi_router.get(f"/api/{id}/get_aanganwadi")
async def get_aanganwadi(id: str):
    aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": aanganwadi}


@aanganwadi_router.put("/api/updateAanganwadi")
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
    return {"status": "ok", "data": child}


@ child_malnutrition.put("/update_child_malnutrition")
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


# Create Supplementary detail


@supp_router.post('/supplementary/', response_model=Supplementary)
def create_supplementary(supplementary: Supplementary):
    supplementary_dict = supplementary.dict()
    inserted_id = SupplementaryCollection.insert_one(
        supplementary_dict).inserted_id
    supplementary.id = str(inserted_id)
    return supplementary


# Read all Supplementary details


@supp_router.get('/supplementary/', response_model=List[Supplementary])
def read_supplementary():
    supplementary_list = []
    for supplementary in SupplementaryCollection.find():
        supplementary['id'] = str(supplementary['_id'])
        del supplementary['_id']
        supplementary_list.append(supplementary)
    return supplementary_list


# Read a single Supplementary detail


@supp_router.get('/supplementary/{supplementary_id}', response_model=Supplementary)
def read_single_supplementary(supplementary_id: str):
    supplementary = SupplementaryCollection.find_one(
        {'_id': ObjectId(supplementary_id)})
    if supplementary:
        supplementary['id'] = str(supplementary['_id'])
        del supplementary['_id']
        return supplementary
    else:
        raise HTTPException(
            status_code=404, detail='Supplementary detail not found')


# Update a Supplementary detail


@supp_router.put('/supplementary/{supplementary_id}', response_model=Supplementary)
def update_supplementary(supplementary_id: str, supplementary: Supplementary):
    updated_supplementary = supplementary.dict(exclude_unset=True)
    result = SupplementaryCollection.update_one(
        {'_id': ObjectId(supplementary_id)}, {'$set': updated_supplementary})
    if result.modified_count == 1:
        updated_supplementary['id'] = supplementary_id
        return updated_supplementary
    elif result.matched_count == 1:
        raise HTTPException(status_code=422, detail='Nothing to update')
    else:
        raise HTTPException(
            status_code=404, detail='Supplementary detail not found')


# Delete a Supplementary detail


@supp_router.delete('/supplementary/{supplementary_id}')
def delete_supplementary(supplementary_id: str):
    result = SupplementaryCollection.delete_one(
        {'_id': ObjectId(supplementary_id)})
    if result.deleted_count == 1:
        return {'message': 'Supplementary detail deleted successfully'}
    else:
        raise HTTPException(
            status_code=404, detail='Supplementary detail not found')


@supplement_details.post('/add_supplement_details')
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


@supplement_details.get('/get_supplements_details')
async def get_supplements_details():
    """
    This function is create for get the supplement details.
    :return: Response status and fetched all data from db
    """
    result = supplements_list_serializer(SupplementDetailsCollection.find())
    return {"status": "ok", "data": result}


@supplement_details.get(f'/{id}/get_supplement_details')
async def get_supplement_details(id: str):
    """
    This function is create to retrieve particular supplement details.
    :param id: id of the supplements to retrieve.
    :return: Response status and a dictionary representing the supplement data in a custom format.
    """
    result = supplements_list_serializer(
        SupplementDetailsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": result}


@supplement_details.put('/update_supplement_details')
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


@supplement_details.delete('/delete_supplement_details')
async def delete_supplement_details(id: str):
    """
    This function is create to delete the supplement details.
    :param id: id of the supplement to be deleted.
    :return: Response status.
    """
    SupplementDetailsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@program_router.post("/programs", response_model=Program)
async def create_program(program: Program):
    program_dict = program.dict()
    program_dict["donor"] = {"_id": ObjectId(
        program.donor.id), "name": program.donor.name}
    program_dict["supplement"] = {"_id": ObjectId(
        program.supplement.id), "name": program.supplement.name}
    result = ProgramsCollection.insert_one(program_dict)
    program.id = str(result.inserted_id)
    return program


@program_router.get("/programs", response_model=List[Program])
async def read_programs():
    programs = []
    for program_dict in ProgramsCollection.find():
        program = Program.from_dict(program_dict)
        programs.append(program)
    return programs


@program_router.get("/programs/{program_id}", response_model=Program)
async def read_program(program_id: str):
    program_dict = ProgramsCollection.find_one({"_id": ObjectId(program_id)})
    if program_dict is None:
        raise HTTPException(status_code=404, detail="Program not found")
    program = Program.from_dict(program_dict)
    return program


@program_router.put("/programs/{program_id}", response_model=Program)
async def update_program(program_id: str, program: Program):
    program_dict = program.dict()
    program_dict["donor"] = {"_id": ObjectId(
        program.donor.id), "name": program.donor.name}
    program_dict["supplement"] = {"_id": ObjectId(
        program.supplement.id), "name": program.supplement.name}
    result = ProgramsCollection.replace_one(
        {"_id": ObjectId(program_id)}, program_dict)
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Program not found")
    program.id = program_id
    return program


@program_router.delete("/programs/{program_id}")
async def delete_program(program_id: str):
    result = ProgramsCollection.delete_one({"_id": ObjectId(program_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Program not found")
    return {"message": "Program deleted successfully"}
