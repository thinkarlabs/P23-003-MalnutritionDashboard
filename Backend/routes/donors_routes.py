from fastapi import APIRouter
from Backend.config.database import DonorsCollection
from Backend.model.model import Donor
from Backend.schemas.schema import donors_list_serializer
from bson import ObjectId

donor_router = APIRouter()


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
