from pydantic import BaseModel




class User(BaseModel):
   username: str
   password: str
   user_type: str



class Ngo(BaseModel):
    name: str
    email: str
    password: str
    location: str
    pincode: int

