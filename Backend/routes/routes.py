from argparse import OPTIONAL
from fastapi import APIRouter, Body
from Backend.model.model import Ngo, User, Donor, Aanganwadi
from Backend.config.database import NgoCollection, UserCollection, AanganwadiCollection
from Backend.config.database import DonorsCollection
from Backend.schemas.schema import ngo_list_serializer, user_list_serializer, donors_list_serializer
from Backend.schemas.schema import aanganwadi_list_serializer
from typing import Union
from bson import ObjectId
from fastapi import HTTPException

user_router = APIRouter()
ngo_router = APIRouter()
aanganwadi_router = APIRouter()


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


donor_router = APIRouter()


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
