from fastapi import APIRouter
from Backend.model.model import Ngo
from Backend.config.database import collection
from Backend.schemas.schema import ngo_addition_serializer

ngo_addition_router = APIRouter()


@ngo_addition_router.post("/ngoAddition")
async def ngo_addition(ngo: Ngo):
    _id = collection.insert_one(dict(ngo))
    added_Ngo = ngo_addition_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_Ngo}
