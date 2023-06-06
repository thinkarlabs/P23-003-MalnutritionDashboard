from fastapi import APIRouter
from Backend.model.model import SupplementaryPacks
from Backend.config.database import SupplementaryCollection
from Backend.schemas.schema import supplementaryPacks_list_serializer
from bson import ObjectId

supp_router = APIRouter()


@supp_router.post('/api/add_supplement_pack/')
async def add_supplement_pack(supplementary: SupplementaryPacks):
    """
    Adds a new supplement pack to the SupplementaryCollection database collection.
    :param supplementary: The supplement pack to be added.
    :return: status of the added supplement pack's data.
    """
    print(supplementary)
    _id = SupplementaryCollection.insert_one(dict(supplementary))
    add_supplementary = supplementaryPacks_list_serializer(
        SupplementaryCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": add_supplementary}


@supp_router.get('/api/get_all_supplement_packs/{program_joining_id}')
async def get_all_supplement_packs_for_a_program(program_joining_id: str):
    """
    Retrieves all supplement packs associated with a specific program from the SupplementaryCollection database collection.
    :param program_joining_id: The unique identifier of the program to retrieve supplement packs for.
    :return: status of the retrieved supplement packs' data.
    """
    supplementary = supplementaryPacks_list_serializer(
        SupplementaryCollection.find({"program_joining_id": str(program_joining_id)}))
    return {"status": "ok", "data": supplementary}


@supp_router.get('/api/get_supplement_pack/{supplementary_id}')
async def get_supplement_pack(supplementary_id: str):
    """
     Retrieves a supplement pack with the specified ID from the SupplementaryCollection database collection.
    :param supplementary_id: The unique identifier of the supplement pack to retrieve.
    :return: status of the retrieved supplement pack's data.
    """
    supplementary = supplementaryPacks_list_serializer(
        SupplementaryCollection.find({"_id": ObjectId(supplementary_id)}))
    return {"status": "ok", "data": supplementary}


@supp_router.put('/api/update_supplement_pack/{supplementary_id}')
async def update_supplement_pack(supplementary_id: str, supplementary: SupplementaryPacks):
    """
    Updates a supplement pack with the specified ID in the SupplementaryCollection database collection.
    :param supplementary_id: The unique identifier of the supplement pack to update
    :param supplementary: The updated supplement pack data.
    :return: status of the updated supplement pack's data.
    """
    SupplementaryCollection.find_one_and_update({"_id": ObjectId(supplementary_id)},
                                                {"$set": dict(supplementary)})
    updated_supplementary = supplementaryPacks_list_serializer(
        SupplementaryCollection.find({"_id": ObjectId(supplementary_id)}))
    return {"status": "ok", "data": updated_supplementary}


@supp_router.delete('/api/delete_supplement_pack/{supplementary_id}')
def delete_supplement_pack(supplementary_id: str):
    """
    Deletes a supplement pack with the specified ID from the SupplementaryCollection database collection.
    :param supplementary_id: The unique identifier of the supplement pack to delete
    :return:  message indicating that the supplement pack was deleted successfully.
    """
    result = SupplementaryCollection.find_one_and_delete(
        {"_id": ObjectId(supplementary_id)})
    return {"message": "supplementary deleted successfully"}

