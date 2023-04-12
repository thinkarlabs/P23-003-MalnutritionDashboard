from fastapi import APIRouter
from Backend.config.database import ChildCollection
from Backend.model.model import Child
from Backend.schemas.schema import child_list_serializer
from bson import ObjectId

child_router = APIRouter()


@child_router.post("/api/add_child")
async def add_child(child: Child):
    _id = ChildCollection.insert_one(dict(child))
    added_child = child_list_serializer(
        ChildCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_child}


@child_router.get("/api/get_childs")
async def get_childs():
    childs = child_list_serializer(ChildCollection.find())
    return {"status": "ok", "data": childs}


@child_router.get("/api/{id}/get_child")
async def get_child(id: str):
    childs = child_list_serializer(
        ChildCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": childs}


@child_router.put("/api/updatechild/{id}")
async def update_child(id: str, child: Child):
    ChildCollection.find_one_and_update({"_id": ObjectId(id)},
                                        {"$set": dict(child)})
    updated_child = child_list_serializer(
        ChildCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_child}


@child_router.delete("/api/deletechild")
async def delete_child(id: str):
    ChildCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
