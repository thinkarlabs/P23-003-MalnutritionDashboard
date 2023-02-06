from fastapi import APIRouter
from Backend.model.model import User
from Backend.config.database import collection, db
from Backend.schemas.schema import user_addition_serializer
from typing import Union
from bson import ObjectId
from fastapi import HTTPException

user_addition_router = APIRouter()


@user_addition_router.post("/userAddition")
async def user_addition(user: User):
    _id = collection.insert_one(dict(user))
    added_User = user_addition_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_User}


@user_addition_router.get("/get_users")
async def get_users():
    users = user_addition_serializer(collection.find())
    return {"status": "ok", "data": users}


@user_addition_router.get(f"/{id}/get_user")
async def get_user(id: str):
    user = user_addition_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": user}

def Validate_User_Object(email,password,user_type):
    collection = db['Malnutrition']
    valid = 0
    for data in collection.find():
        if ((data['username'] == email) & (data['password'] == password ) & (data['user_type'] == user_type)):
            valid = 1
    return valid




@user_addition_router.get("/isvaliduser")
async def read_item(username:str, password: Union[str, None] = None,user_type: Union[str, None] = None):
    valid = Validate_User_Object (username,password,user_type)
    if valid == 0:
        raise HTTPException(status_code=400, detail="Invalid user request")
        #return {"response":"Invalid username or password"}
    else:
        raise HTTPException(status_code=200, detail="Successfully login")
        #return {"response":"Successfully login"}














