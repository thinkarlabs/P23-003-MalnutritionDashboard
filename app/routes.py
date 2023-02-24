from app.model import User,Ngo
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer
from fastapi import FastAPI, APIRouter, Depends,Response,status,Body

sign_router = APIRouter()
@sign_router.get("/")
async def root():
    return {"message": "Welcome to Think Nutrition"}
ngo_users=[
{
    "id":1,
    "name":"alea",
    "contactPersonName":"alekhya",
    "contactPersonEmail":"alea@gmail.com",
    "contactPersonPhone":1234567891,
    "contactPersonPassword":"all1234",
    "location":"Ongole",
    "pincode":523001
},
{
    "id":2,
    "name":"lucky",
    "contactPersonName":"anu",
    "contactPersonEmail":"anu@gmail.com",
    "contactPersonPhone":1234567890,
    "contactPersonPassword":"anu1234",
    "location":"Ongole",
    "pincode":523001
}
]
users =[
    {
        "username":"alekhya2427@gmail.com",
        "password":"all123",
        "user_type":"admin"
    },
    {
        "username":"ram@gmail.com",
        "password":"123",
        "user_type":"admin"
    }
]

# creating users
@sign_router.post("/user/signup", tags=["user"])
def user_signup(user: User = Body(default=None)):
    print("you are in signnup", user)
    users.append(user.dict())
    print("aftersignnup", users)
    return signJWT(user.username)


# validating user credentials are matching or not
def check_user(data: User):
    print("validating user", data)
    for user in users:
        print("username.......... : ", user['username'])
        print("password : ", data.password)
        if data.username == user['username'] and data.password == user['password']:
            return True
    return False


# User login to generate token
@sign_router.post("/user/login", tags=["user"])
def user_login(response: Response, user: User = Body(default=None)):
    print("The data-----------------", user)
    if check_user(user):
        # print(signJwt(user.email))
        token = signJWT(user.username)
        response.set_cookie(key="access_token", value=f"Bearer {token['access token']}", httponly=True)
        return {"access_token": token['access token'], "token_type": "bearer"}
    else:
        return {"error": "Invalid Login"}


# Getting ngo users
@sign_router.get("/get_ngo_users")
async def get_users():
    print("All ngo details : ", ngo_users)
    return {"data": ngo_users}


# Adding Ngo users after admin successful login
@sign_router.post("/post_ngo_users", dependencies=[Depends(JWTBearer())])
def add_posts(ngo: Ngo):
    print("ngo dictionary", ngo.dict())
    ngo.id = len(ngo_users) + 1
    ngo_users.append(ngo.dict())
    return {"info": "post added"}


# Get Ngo by ID
@sign_router.get("/ngo/{id}", )
def get_one_post(id: int):
    if id > len(ngo_users):
        print("id is not matching")
        return {"error": "Post id not exist"}

    for ngo in ngo_users:
        if ngo["id"] == id:
            print("ID matched")
            return {"data": ngo}
