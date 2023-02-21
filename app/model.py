from pydantic import BaseModel, EmailStr, validator, Field


class User(BaseModel):
    username: EmailStr
    password: str
    user_type: str
    class Config:
        schema_extra ={
            "user_credentials":{
                "username":"alekhya@gmail.com",
                "password":"ale",
                "user_type":"admin"
            }
        }


class Ngo(BaseModel):
    id:int 
    ngoName: str = Field(default=None)
    contactPersonName: str
    contactPersonEmail: EmailStr
    contactPersonPhone: int = Field(default=None)
    contactPersonPassword: str
    location: str
    pincode: int
    class Config:
        schema_extra ={
            "add_ngo":{
                "id":1,
                "ngoName":"alea",
                "contactPersonName":"alekhya",
                "contactPersonEmail":"alea@gmail.com",
                "contactPersonPhone":1234567890,
                "contactPersonPassword":"all1234",
                "location":"Ongole",
                "pincode":523001
            }
        }






