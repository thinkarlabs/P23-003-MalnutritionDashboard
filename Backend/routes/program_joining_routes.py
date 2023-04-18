from fastapi import APIRouter, HTTPException
from Backend.model.model import ProgramJoining
from Backend.config.database import ProgramJoiningCollection, ProgramsCollection, AanganwadiCollection
from Backend.schemas.schema import programjoining_list_serializer, program_list_serializer
from bson import ObjectId

program_joining = APIRouter()


@program_joining.post("/api/Add_program_joining")
async def add_program_joining(programs: ProgramJoining):
    """
    Adds a program joining record to the database.
    :programs: An instance ,containing the data for the program joining record to be added.
    :Returns:dict: A dictionary containing the status of the operation and the data of the added
    program joining record, serialized using the programjoining_list_serializer function.
    :Raises:HTTPException: If the invite code or Aaganwadi ID is invalid, returns a 404 status code
    with a message indicating which parameter is invalid.
    """
    result = ProgramsCollection.find_one({"invite_code": programs.invite_code})
    identifedAaganwadi = AanganwadiCollection.find_one(
        {"_id": ObjectId(programs.aanganwadi_id)})
    if not result:
        raise HTTPException(status_code=404, detail="Invalid invite code")
    elif not identifedAaganwadi:
        raise HTTPException(status_code=404, detail="Invalid Aaganwadi")
    else:
        programs.program_id = str(result['_id'])
        _id = ProgramJoiningCollection.insert_one(dict(programs))
        add_joining_details = programjoining_list_serializer(
            ProgramJoiningCollection.find({"_id": _id.inserted_id}))
        return {"status": "ok", "data": add_joining_details}


@program_joining.get("/api/get_programs_joining_details")
async def get_programs():
    """
    Returns a list of all program joining records in the database.
    :Returns:dict: status of the operation and the data of all program
    joining records in the database, serialized using the programjoining_list_serializerfunction.
    """
    programs = programjoining_list_serializer(
        ProgramJoiningCollection.find())
    return {"status": "ok", "data": programs}


@program_joining.get("/api/get_program_joining_details/{aanganwadi_id}")
async def get_program_joining_details(aanganwadi_id: str):
    """
    Returns a summary of all program joinings for the specified Aanganwadi.
    :aanganwadi_id (str): The ID of the Aanganwadi for which to retrieve program joinings.
    :Returns:dict: the status of the operation and a list of program joining
    details for the specified Aanganwadi. The list contains a dictionary for each program
    joining record, with keys for the program joining ID, donor name, supplement name,
    from date, and to date.
    """

    list_of_program_joining_summary = []
    program_joining_array = programjoining_list_serializer(
        ProgramJoiningCollection.find({"aanganwadi_id": str(aanganwadi_id)}))
    print(program_joining_array)
    for program_joining_obj in program_joining_array:
        program_id = program_joining_obj["program_id"]
        program_joining_id = program_joining_obj["id"]
        program_details = program_list_serializer(
            ProgramsCollection.find({"_id": ObjectId(program_id)}))
        if len(program_details) > 0:
            donor_name = program_details[0]["donor_name"]
            supplement_name = program_details[0]["supplement_name"]
            from_date = program_details[0]["from_date"]
            to_date = program_details[0]["to_date"]
            program_joining_object = {
                "program_joining_id": program_joining_id,
                "donor_name": donor_name,
                "supplement_name": supplement_name,
                "from_date": from_date,
                "to_date": to_date
            }
            list_of_program_joining_summary.append(program_joining_object)
    return {"status": "ok", "data": list_of_program_joining_summary}

