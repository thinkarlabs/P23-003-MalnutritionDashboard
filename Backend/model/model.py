from pydantic import BaseModel


class Ngo(BaseModel):
    name: str
    email: str
    password: str
    location: str
    pincode: int
