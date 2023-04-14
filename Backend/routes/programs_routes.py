from fastapi import APIRouter, HTTPException
from Backend.model.model import Program
from Backend.config.database import ProgramsCollection, DonorsCollection, SupplementDetailsCollection
from Backend.schemas.schema import program_list_serializer
from bson import ObjectId

program_router = APIRouter()


@program_router.post("/api/add_program")
async def add_program(program: Program):
    """
   Adds a new program to the ProgramsCollection collection in the database.
   :Param:program (Program): A Program object containing details of the program, such as donor_id and supplements_details_id.
   :Returns:dict: A dictionary with a "status" key and a "data" key containing the added program details.
   :Raises: HTTPException: If the donor_id or supplements_details_id do not exist in their respective collections,
   an HTTPException with a 404 status code and an error message is raised.

    """
    donor_details = DonorsCollection.find_one(
        {"_id": ObjectId(program.donor_id)})
    suplement_details = SupplementDetailsCollection.find_one(
        {"_id": ObjectId(program.supplements_details_id)})
    if not donor_details and suplement_details:
        raise HTTPException(status_code=404, detail="input are missing")
    program.donor_name = str(donor_details['name'])
    program.supplement_name = str(suplement_details['name'])
    _id = ProgramsCollection.insert_one(dict(program))
    added_programs = program_list_serializer(ProgramsCollection.find(
        {"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_programs}


@program_router.get("/api/get_programs")
async def get_programs():
    """
    Retrieves a list of all programs from the database.
    :Returns: A dictionary containing the status of the operation and the retrieved programs data.

    """
    programs = program_list_serializer(
        ProgramsCollection.find())
    return {"status": "ok", "data": programs}


@program_router.get("/api/get_program/{id}")
async def get_program(id: str):
    """
    Returns a single program with the specified ID.
    :id (str): The ID of the program to retrieve.
    :Returns: dict: A dictionary containing the status of the operation and the data of the retrieved program.
    """
    result = program_list_serializer(
        ProgramsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": result}


@program_router.put("/api/update_program/{id}")
async def update_program(id: str, program: Program):
    """
    Update an existing program with given ID.
    :id (str): The ID of the program to be updated.
    :program (Program): The program object containing updated information.
    :Returns:dict: A dictionary containing the status of the update operation and the updated program data.
    :Raises:HTTPException: If the specified ID is invalid or the program object is missing required fields.

    """
    ProgramsCollection.find_one_and_update({"_id": ObjectId(id)},
                                           {"$set": dict(program)})
    updated_value = program_list_serializer(
        ProgramsCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": updated_value}


@program_router.delete("/api/delete_program/{id}")
async def delete_program(id: str):
    """
    Deletes the program with the specified ID from the database.
    :id (str): The ID of the program to be deleted.
    :Returns:dict: A dictionary containing a "status" key with the value "ok",
    and an empty "data" key indicating that no data was returned.
    """
    ProgramsCollection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
