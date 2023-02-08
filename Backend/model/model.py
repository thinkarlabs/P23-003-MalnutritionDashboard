from pydantic import BaseModel


class User(BaseModel):
   username: str
   password: str
   user_type: str


class Ngo(BaseModel):
    ngoName: str
    contactPersonName: str
    contactPersonEmail: str
    contactPersonPhone: int
    contactPersonPassword: str

class Donor(BaseModel):
    name: str
    contactperson: str
    email: str
    phone: int
