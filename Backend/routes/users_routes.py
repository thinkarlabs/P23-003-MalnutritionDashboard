from fastapi import APIRouter, HTTPException
from Backend.model.model import User
from Backend.config.database import UserCollection
from Backend.schemas.schema import user_list_serializer
from Backend.config.database import NgoCollection, AanganwadiCollection
from Backend.schemas.schema import ngo_list_serializer, aanganwadi_list_serializer
from bson import ObjectId

user_router = APIRouter()


@user_router.post("/api/create_user")
async def create_user(user: User):
    """
     Creates a new user in the UserCollection and returns the added user's data.
     :param: user (User): A User object containing the user's information.
     :Returns:dict: A dictionary containing the status of the operation and the added user's data.

    """
    _id = UserCollection.insert_one(dict(user))
    added_user = user_list_serializer(
        UserCollection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": added_user}


@user_router.get("/api/get_users")
async def get_users():
    """
    Retrieves a list of all users from the UserCollection and returns the user data.
    :Returns: dict: A dictionary containing the status of the operation and a list of user data.

    """
    users = user_list_serializer(UserCollection.find())
    return {"status": "ok", "data": users}


@user_router.get(f"/api/{id}/get_user")
async def get_user(id: str):
    """
    Retrieves a single user from the UserCollection based on their unique identifier.
    :id (str): The unique identifier of the user to retrieve.
    :Returns:dict: A dictionary containing the status of the operation and the user data.
    """
    user = user_list_serializer(UserCollection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": user}


def Validate_User_Object(username, password):
    """
    Validates the given username and password against user data stored in the UserCollection, NgoCollection,
    and AanganwadiCollection. Returns a User object with the identified user type.
    :username (str): The username of the user to validate.
    :password (str): The password of the user to validate.
    :Returns:
            User: A User object representing the identified user. The object has the following fields:
                - username (str): The username of the identified user.
                - password (str): The password of the identified user.
                - user_type (str): The type of the identified user, which can be one of the following:
                    - 'admin': If the identified user is an admin user.
                    - 'ngo': If the identified user is an NGO contact person.
                    - 'aaganwadi': If the identified user is an Aanganwadi contact person.
        """
    valid = 0
    userSearched = user_list_serializer(UserCollection.find(
        {'username': str(username), 'password': str(password)}))
    ngoSearched = ngo_list_serializer(
        NgoCollection.find({"contactPersonName": str(username), "contactPersonPassword": str(password)}))
    aaganwadiSearched = aanganwadi_list_serializer(AanganwadiCollection.find(
        {'contactPersonName': str(username), 'contactPersonPassword': str(password)}))
    identifiedUser = User(username=str(username), password=str(
        password), user_type=str(""))
    if (ngoSearched):
        identifiedUser.user_type = "ngo"
    elif (aaganwadiSearched):
        identifiedUser.user_type = "aaganwadi"
    elif (userSearched):
        identifiedUser.user_type = "admin"
    print('identifiedUser' + str(identifiedUser))
    return identifiedUser


@user_router.post("/api/isvaliduser")
async def read_item(requestUser: User):
    """
    The read_item function takes a User object as input and validates the provided username
    and password using the Validate_User_Object function.
    :param:requestUser: A User object containing the username and password of the user attempting to log in.
    :returns: If the credentials are valid, returns a dictionary with a "status" key set to "ok" and a "data" key set
    to an identifiedUser object. If the credentials are invalid, raises an HTTPException with a status code of 404.
    """
    identifiedUser = Validate_User_Object(
        requestUser.username, requestUser.password)
    if identifiedUser.user_type == "":
        raise HTTPException(
            status_code=404, detail="Invalid username or password")
        # return {"response": "Invalid username or password"}
    else:
        return {"status": "ok", "data": identifiedUser}
        # raise HTTPException(status_code=200, detail="Successful login")
        # return {"response":"Successful login"}

