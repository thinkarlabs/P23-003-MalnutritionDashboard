from fastapi import APIRouter
from Backend.model.model import Ngo
from Backend.config.database import collection
from Backend.schemas.schema import ngo_addition_serializer
from bson import ObjectId

ngo_addition_router = APIRouter()


@ngo_addition_router.post("/ngoAddition")
async def ngo_addition(ngo: Ngo):
    _id = collection.insert_one(dict(ngo))
    added_Ngo = ngo_addition_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_Ngo}


@ngo_addition_router.get("/get_ngos")
async def get_ngos():
    ngos = ngo_addition_serializer(collection.find())
    return {"status": "ok", "data": ngos}


@ngo_addition_router.get(f"/{id}/get_ngo")
async def get_ngo(id: str):
    ngo = ngo_addition_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": ngo}
