from argparse import OPTIONAL
from fastapi import APIRouter
from Backend.model.model import User
from Backend.config.database import collection, db
from Backend.schemas.schema import user_list_serializer
from typing import Union
from bson import ObjectId
from fastapi import HTTPException

user_router = APIRouter()

@user_router.post("/userAddition")
async def user_addition(user: User):
    _id = collection.insert_one(dict(user))
    added_User = user_list_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_User}

@user_router.get("/get_users")
async def get_users():
    users = user_list_serializer(collection.find())
    return {"status": "ok", "data": users}


@user_router.get(f"/{id}/get_user")
async def get_user(id: str):
    user = user_list_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": user}

def Validate_User_Object(email,password,user_type):
    collection = db['Malnutrition']
    valid = 0
    for data in collection.find():
        if ((data['username'] == email) & (data['password'] == password ) & (data['user_type'] == user_type)):
            valid = 1
    return valid

@user_router.get("/isvaliduser")
async def read_item(username:str, password: Union[str, None] = None,user_type: Union[str, None] = None):
    valid = Validate_User_Object (username,password,user_type)
    if valid == 0:
        raise HTTPException(status_code=404, detail="user not found")
        #return {"response":"Invalid username or password"}
    else:
        raise HTTPException(status_code=200, detail="Successful login")
        #return {"response":"Successful login"}















from Backend.model.model import Ngo
from Backend.config.database import Ngocollection
from Backend.schemas.schema import ngo_list_serializer
from bson import ObjectId

ngo_router = APIRouter()


@ngo_router.post("/addNgo")
async def ngo_addition(ngo: Ngo):
    _id = Ngocollection.insert_one(dict(ngo))
    added_Ngo = ngo_list_serializer(
        Ngocollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_Ngo}


@ngo_router.get("/getNgos")
async def get_ngos():
    ngos = ngo_list_serializer(Ngocollection.find())
    return {"status": "ok", "data": ngos}


@ngo_router.get(f"/{id}/get_ngo")
async def get_ngo(id: str):
    ngo = ngo_list_serializer(
        Ngocollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": ngo}


@ngo_router.delete("/delete_ngo/{id}")
async def delete_ngo(id: str):
    Ngocollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
