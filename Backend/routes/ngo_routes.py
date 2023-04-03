from fastapi import APIRouter
from Backend.model.model import Ngo
from Backend.schemas.schema import ngo_list_serializer
from Backend.config.database import NgoCollection
from bson import ObjectId

ngo_router = APIRouter()


@ngo_router.post("/api/create_ngo")
async def create_ngo(ngo: Ngo):
    """
    This function is created for new NGO details.
    :param ngo: ngo contain Dictionary value which is Ngo data
    :return: status of the response and newly added NGO data
    """
    _id = NgoCollection.insert_one(dict(ngo))
    added_ngo = ngo_list_serializer(
        NgoCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_ngo}


@ngo_router.get("/api/getNgos")
async def get_ngos():
    """
    This function is created for fetch the all NGO data from database.
    :return:
    """
    ngos = ngo_list_serializer(NgoCollection.find())
    return {"status": "ok", "data": ngos}


@ngo_router.get("/api/{id}/get_ngo")
async def get_ngo(id: str):
    """
    This function is created for fetch the particular ngo data from DB.
    :param id: Retrieve a single item by id.
    :return: status of the response and fetch data with id.
    """
    ngo = ngo_list_serializer(
        NgoCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": ngo}


@ngo_router.put("/api/ngos/{ngo_id}")
async def update_ngo(ngo_id: str, ngo: Ngo):
    """
    Update an existing Ngo data by id.
    :param ngo_id: ngo_id of the ngo data need to update.
    :param ngo:  a dictionary containing the updated NGO data.
    :return: status of the response and updated data.
    """
    NgoCollection.find_one_and_update({"_id": ObjectId(ngo_id)},
                                      {"$set": dict(ngo)})
    updated_value = ngo_list_serializer(
        NgoCollection.find({"_id": ObjectId(ngo_id)}))
    return {"status": "ok", "data": updated_value}


@ngo_router.delete("/api/delete_ngo/{id}")
async def delete_ngo(id: str):
    """
    Delete an existing Ngo data by id.
    :param id: id of the ngo data which need to delete.
    :return: status of the response
    """
    NgoCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": "successfully deleted"}
