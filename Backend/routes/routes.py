from argparse import OPTIONAL
from fastapi import APIRouter
from Backend.model.model import Ngo, User
from Backend.config.database import NgoCollection, UserCollection
from Backend.schemas.schema import ngo_list_serializer, user_list_serializer
from typing import Union
from bson import ObjectId
from fastapi import HTTPException

user_router = APIRouter()
ngo_router = APIRouter()


@user_router.post("/userAddition")
async def user_addition(user: User):
    _id = UserCollection.insert_one(dict(user))
    added_User = user_list_serializer(UserCollection.find({"_id": _id.inserted_id}))
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


@ngo_router.post("/addNgo")
async def ngo_addition(ngo: Ngo):
    _id = NgoCollection.insert_one(dict(ngo))
    added_Ngo = ngo_list_serializer(
        NgoCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_Ngo}


@ngo_router.get("/getNgos")
async def get_ngos():
    ngos = ngo_list_serializer(NgoCollection.find())
    return {"status": "ok", "data": ngos}


@ngo_router.get(f"/{id}/get_ngo")
async def get_ngo(id: str):
    ngo = ngo_list_serializer(
        NgoCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": ngo}


@ngo_router.delete("/delete_ngo/{id}")
async def delete_ngo(id: str):
    NgoCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
