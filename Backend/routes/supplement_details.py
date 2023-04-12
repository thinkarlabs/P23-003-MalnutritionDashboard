from fastapi import APIRouter
from Backend.config.database import SupplementDetailsCollection
from Backend.model.model import SupplementsDetail
from Backend.schemas.schema import supplements_list_serializer
from bson import ObjectId

supplement_details = APIRouter()

@supplement_details.post('/api/add_supplement_details')
def add_supplement_details(supplement: SupplementsDetail):
    """
    This function is create for add the supplement details.
    :param supplement: A Pydantic model representing the supplement data to be created.
    :return: Response status and newly created supplement data.
    """
    _id = SupplementDetailsCollection.insert_one(dict(supplement))
    added_supplement = supplements_list_serializer(
        SupplementDetailsCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_supplement}


@supplement_details.get('/api/get_supplements_details')
async def get_supplements_details():
    """
    This function is create for get the supplement details.
    :return: Response status and fetched all data from db
    """
    result = supplements_list_serializer(SupplementDetailsCollection.find())
    return {"status": "ok", "data": result}


@supplement_details.get('/api/{id}/get_supplement_details')
async def get_supplement_details(id: str):
    """
    This function is create to retrieve particular supplement details.
    :param id: id of the supplements to retrieve.
    :return: Response status and a dictionary representing the supplement data in a custom format.
    """
    result = supplements_list_serializer(
        SupplementDetailsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": result}


@supplement_details.put('/api/update_supplement_details/{id}')
async def update_supplement_details(id: str, supplement: SupplementsDetail):
    """
    This function is create to update the supplement details.
    :param id: id of the supplement to be updated.
    :param supplement: The pydantic model representing the updated supplement data.
    :return: Response status and updated supplement data.
    """
    SupplementDetailsCollection.find_one_and_update({"_id": ObjectId(id)},
                                                    {"$set": dict(supplement)})
    updated_value = supplements_list_serializer(
        SupplementDetailsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_value}


@supplement_details.delete('/api/delete_supplement_details/{id}')
async def delete_supplement_details(id: str):
    """
    This function is create to delete the supplement details.
    :param id: id of the supplement to be deleted.
    :return: Response status.
    """
    SupplementDetailsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
