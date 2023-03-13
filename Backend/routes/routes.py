from argparse import OPTIONAL
from fastapi import APIRouter, Body
from Backend.model.model import Ngo, User, Donor, Aanganwadi, Child, ChildMalnutrition
from Backend.config.database import NgoCollection, UserCollection, AanganwadiCollection, ChildCollection
from Backend.config.database import DonorsCollection, ChildMalnutritionCollection
from Backend.schemas.schema import ngo_list_serializer, user_list_serializer, donors_list_serializer
from Backend.schemas.schema import aanganwadi_list_serializer, child_list_serializer, child_malnutrition_list_serializer
from typing import Union



user_router = APIRouter()
ngo_router = APIRouter()
donor_router = APIRouter()
aanganwadi_router = APIRouter()
child_router = APIRouter()
child_malnutrition = APIRouter()


@user_router.post("/create_user")
async def create_user(user: User):
    _id = UserCollection.insert_one(dict(user))
    added_User = user_list_serializer(
        UserCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_User}


@user_router.get("/get_users")
async def get_users():
    users = user_list_serializer(UserCollection.find())
    return {"status": "ok", "data": users}


@user_router.get(f"/{id}/get_user")
async def get_user(id: str):
    user = user_list_serializer(UserCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": user}


def Validate_User_Object(email, password, user_type):
    valid = 0
    for user in UserCollection.find():
        if (user['username'] == email) & (user['password'] == password) & (user['user_type'] == user_type):
            valid = 1
    return valid


@user_router.get("/isvaliduser")
async def read_item(username: str, password: Union[str, None] = None, user_type: Union[str, None] = None):
    valid = Validate_User_Object(username, password, user_type)
    if valid == 0:
        raise HTTPException(status_code=404, detail="user not found")
        # return {"response":"Invalid username or password"}
    else:
        raise HTTPException(status_code=200, detail="Successful login")
        # return {"response":"Successful login"}


@ngo_router.post("/create_ngo")
async def create_ngo(ngo: Ngo):
    _id = NgoCollection.insert_one(dict(ngo))
    added_Ngo = ngo_list_serializer(
        NgoCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_Ngo}


@ngo_router.get("/getNgos")
async def get_ngos():
    ngos = ngo_list_serializer(NgoCollection.find())
    return {"status": "ok", "data": ngos}


@ngo_router.get("/get_ngo/{id}")
async def get_ngo(id: str):
    ngo = ngo_list_serializer(
        NgoCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": ngo}


@ngo_router.delete("/delete_ngo/{id}")
async def delete_ngo(id: str):
    NgoCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@ngo_router.put("/ngos/{ngo_id}")
async def update_ngo(ngo_id: str, ngo: Ngo):
    result = NgoCollection.update_one({"_id": ngo_id}, {"$set": ngo.dict()})
    return {"updated": result.modified_count}


@donor_router.post("/donors")
async def create_donor(donor: Donor):
    _id = DonorsCollection.insert_one(dict(donor))
    donor = donors_list_serializer(
        DonorsCollection.find({"id": _id.inserted_id}))
    return {"status": "ok", "data": donor}


@donor_router.get("/getdonors")
async def get_donors():
    donors = donors_list_serializer(DonorsCollection.find())
    return {"status": "ok", "data": donors}


@donor_router.get(f"/{id}/get_donor")
async def get_donor(id: str):
    donor = donors_list_serializer(
        DonorsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": donor}


@donor_router.delete("/delete_donor/{id}")
async def delete_donor(id: str):
    DonorsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@donor_router.put("/donors/{donor_id}")
async def update_donor(donor_id: str, donor: Donor):
    result = DonorsCollection.update_one(
        {"_id": donor_id}, {"$set": donor.dict()})
    return {"updated": result.modified_count}


@aanganwadi_router.post("/addAanganwadi")
async def aanganwadi_addition(aanganwadi: Aanganwadi):
    _id = AanganwadiCollection.insert_one(dict(aanganwadi))
    added_Aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_Aanganwadi}


@aanganwadi_router.get("/getAanganwadis")
async def get_aanganwadis():
    aanganwadis = aanganwadi_list_serializer(AanganwadiCollection.find())
    return {"status": "ok", "data": aanganwadis}


@aanganwadi_router.get(f"/{id}/get_aanganwadi")
async def get_aanganwadi(id: str):
    aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": aanganwadi}


@aanganwadi_router.put("/updateAanganwadi")
async def update_aanganwadi(id: str, aanganwadi: Aanganwadi):
    AanganwadiCollection.find_one_and_update({"_id": ObjectId(id)},
                                             {"$set": dict(aanganwadi)})
    aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": aanganwadi}


@aanganwadi_router.delete("/delete_aanganwadi/{id}")
async def delete_aanganwadi(id: str):
    AanganwadiCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@child_router.post("/add_child")
async def add_child(child: Child):
    _id = ChildCollection.insert_one(dict(child))
    added_child = child_list_serializer(ChildCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_child}


@child_router.get("/get_childs")
async def get_childs():
    childs = child_list_serializer(ChildCollection.find())
    return {"status": "ok", "data": childs}


@child_router.get(f"/{id}/get_child")
async def get_child(id: str):
    childs = child_list_serializer(
        ChildCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": childs}


@child_router.put("/updateChild")
async def update_child(id: str, child: Child):
    ChildCollection.find_one_and_update({"_id": ObjectId(id)},
                                        {"$set": dict(child)})
    childs = child_list_serializer(
        ChildCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": childs}


@child_router.delete("/deleteChild")
async def delete_child(id: str):
    ChildCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}


@child_malnutrition.post("/childMalnutrion_Add")
async def child_malnutrition_add(child: ChildMalnutrition, child_id: str):
    if not ChildCollection.find_one({"_id": ObjectId(child_id)}):
        raise HTTPException(status_code=404, detail="Child not found")
    _id = ChildMalnutritionCollection.insert_one(dict(child))
    added_malnutrition_child = child_malnutrition_list_serializer(ChildMalnutritionCollection.find(
        {"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_malnutrition_child}


@child_malnutrition.get("/get_child_Malnutritions")
async def get_child_malnutritions():
    childs = child_malnutrition_list_serializer(ChildMalnutritionCollection.find())
    return {"status": "ok", "data": childs}


@child_malnutrition.get(f"/{id}/get_child_malnutrition")
async def get_child_malnutrition(id: str):
    child = child_malnutrition_list_serializer(
        ChildMalnutritionCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": child}


@child_malnutrition.put("/update_child_malnutrition")
async def update_child_malnutrition(id: str, childs: ChildMalnutrition):
    ChildMalnutritionCollection.find_one_and_update({"_id": ObjectId(id)},
                                                    {"$set": dict(childs)})
    updated_value = child_malnutrition_list_serializer(
        ChildMalnutritionCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_value}


@child_malnutrition.delete("/deleteChild_malnutrition")
async def delete_child(id: str):
    ChildMalnutritionCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}

from fastapi import APIRouter, HTTPException
from bson import ObjectId
from typing import List
from Backend.config.database import SupplementaryCollection
from Backend.model.model import Supplementary
supp_router = APIRouter()

# Create Supplementary detail
@supp_router.post('/supplementary/', response_model=Supplementary)
def create_supplementary(supplementary: Supplementary):
    supplementary_dict = supplementary.dict()
    inserted_id = SupplementaryCollection.insert_one(supplementary_dict).inserted_id
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
    supplementary = SupplementaryCollection.find_one({'_id': ObjectId(supplementary_id)})
    if supplementary:
        supplementary['id'] = str(supplementary['_id'])
        del supplementary['_id']
        return supplementary
    else:
        raise HTTPException(status_code=404, detail='Supplementary detail not found')


# Update a Supplementary detail
@supp_router.put('/supplementary/{supplementary_id}', response_model=Supplementary)
def update_supplementary(supplementary_id: str, supplementary: Supplementary):
    updated_supplementary = supplementary.dict(exclude_unset=True)
    result = SupplementaryCollection.update_one({'_id': ObjectId(supplementary_id)}, {'$set': updated_supplementary})
    if result.modified_count == 1:
        updated_supplementary['id'] = supplementary_id
        return updated_supplementary
    elif result.matched_count == 1:
        raise HTTPException(status_code=422, detail='Nothing to update')
    else:
        raise HTTPException(status_code=404, detail='Supplementary detail not found')


# Delete a Supplementary detail
@supp_router.delete('/supplementary/{supplementary_id}')
def delete_supplementary(supplementary_id: str):
    result = SupplementaryCollection.delete_one({'_id': ObjectId(supplementary_id)})
    if result.deleted_count == 1:
        return {'message': 'Supplementary detail deleted successfully'}
    else:
        raise HTTPException(status_code=404, detail='Supplementary detail not found')










