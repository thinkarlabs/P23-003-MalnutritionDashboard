from fastapi import APIRouter
from Backend.model.model import Aanganwadi
from Backend.config.database import AanganwadiCollection
from Backend.schemas.schema import aanganwadi_list_serializer
from bson import ObjectId

aanganwadi_router = APIRouter()


@aanganwadi_router.post("/api/addAanganwadi")
async def aanganwadi_addition(aanganwadi: Aanganwadi):
    """
     This function is create to add new Aanganwadi details.
    :param aanganwadi: aanganwadi contain Dictionary value which is anganwadi data
    :return: response of newly added Aanganwadi data

    """
    _id = AanganwadiCollection.insert_one(dict(aanganwadi))
    added_aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_aanganwadi}


@aanganwadi_router.get("/api/getAanganwadis")
async def get_aanganwadis():
    """
    This function is created for fetch the all Aanganwadis data from database.
    :return: gives the response of all added Aanganwadi data
    """
    aanganwadis = aanganwadi_list_serializer(AanganwadiCollection.find())
    return {"status": "ok", "data": aanganwadis}


@aanganwadi_router.get("/api/{id}/get_aanganwadi")
async def get_aanganwadi(id: str):
    """
    This function is created for fetch the particular aanganwadi data from database.
    :param id: Retrieve a single item by id.
    :return: status of the response and fetch data with id.

    """
    aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": aanganwadi}


@aanganwadi_router.put("/api/updateAanganwadi/{id}")
async def update_aanganwadi(id: str, aanganwadi: Aanganwadi):
    """
     Update an existing Aanganwadi data by id.
    :param id: id of the Aanganwadi data need to update.
    :param aanganwadi:  a dictionary containing the updated Aanganwadi data.
    :return: status of the response and updated data.

    """
    AanganwadiCollection.find_one_and_update({"_id": ObjectId(id)},
                                             {"$set": dict(aanganwadi)})
    aanganwadi = aanganwadi_list_serializer(
        AanganwadiCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": aanganwadi}


@aanganwadi_router.delete("/api/delete_aanganwadi/{id}")
async def delete_aanganwadi(id: str):
    """
     Delete an existing aanganwadi data by id.
    :param id: id of the aanganwadi data which need to delete.
    :return: status of the response

    """
    AanganwadiCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
