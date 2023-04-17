from fastapi import APIRouter, HTTPException
from Backend.model.model import ChildMalnutrition
from Backend.config.database import ChildMalnutritionCollection, ChildCollection
from Backend.schemas.schema import child_malnutrition_list_serializer
from bson import ObjectId


child_malnutrition = APIRouter()


@child_malnutrition.post("/api/childMalnutrion_Add")
async def child_malnutrition_add(child: ChildMalnutrition):
    """
    This function is created for add the child malnutrition details basis on child id.
    :param child: A Pydantic model representing ChildMalnutrition data to be created.
    :return: Response status and newly created ChildMalnutrition data.
    """
    if not ChildCollection.find_one({"_id": ObjectId(child.child_id)}):
        raise HTTPException(status_code=404, detail="Child not found")
    _id = ChildMalnutritionCollection.insert_one(dict(child))
    added_malnutrition_child = child_malnutrition_list_serializer(ChildMalnutritionCollection.find(
        {"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_malnutrition_child}


@child_malnutrition.get("/api/get_child_Malnutritions")
async def get_child_malnutritions():
    """
    This function is created for retrieve all child malnutrition data from db.
    :return: Response status and fetched data from db.
    """
    childs = child_malnutrition_list_serializer(
        ChildMalnutritionCollection.find())
    return {"status": "ok", "data": childs}


@child_malnutrition.get("/api/{child_id}/get_child_malnutrition_stats")
async def get_child_malnutrition_stats(child_id: str):
    """
    This function is create for get the particular child malnutrition data.
    :param id: id of the ChildMalnutrition to retrieve.
    :return: Response status and fetched particular data.
    """
    child = child_malnutrition_list_serializer(
        ChildMalnutritionCollection.find({"child_id": str(child_id)}))
    print(child)
    return {"status": "ok", "data": child}


@child_malnutrition.put("/api/update_child_malnutrition")
async def update_child_malnutrition(id: str, childs: ChildMalnutrition):
    """
    This function is create for update the child malnutrition details.
    :param id: id of the ChildMalnutrition to be updated.
    :param childs: The pydantic model representing the updated ChildMalnutrition data.
    :return: Response status and updated ChildMalnutrition data.
    """
    ChildMalnutritionCollection.find_one_and_update({"_id": ObjectId(id)},
                                                    {"$set": dict(childs)})
    updated_value = child_malnutrition_list_serializer(
        ChildMalnutritionCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_value}


@child_malnutrition.delete("/deleteChild_malnutrition")
async def delete_child(id: str):
    """
    This function is create for delete the child malnutrition details.
    :param id: id of the ChildMalnutrition to be deleted
    :return: Response status
    """
    ChildMalnutritionCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
