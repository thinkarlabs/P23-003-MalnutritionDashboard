from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    username: str
    password: str
    user_type: str


class Ngo(BaseModel):
    ngoName: str
    contactPersonName: str
    contactPersonEmail: EmailStr
    contactPersonPhone: int
    contactPersonPassword: str
    location: str
    pincode: int

    @validator("ngoName")
    def val(cls, ngoName):
        for i in ngoName:
            if i.isalpha():
                continue
            elif i == ' ':
                continue
            else:
                raise ValueError("not accepted")

    @validator("contactPersonName")
    def name_validation(cls, contactPersonName):
        for i in contactPersonName:
            if i.isalpha():
                continue
            elif i == ' ':
                continue
            else:
                raise ValueError("only alphabet acceptable")
        return contactPersonName.title()

    @validator("contactPersonPhone")
    def phone_number_validation(cls, contactPersonPhone):
        if not len(str(contactPersonPhone)) == 10:
            raise ValueError("This field should not be empty, and should not be less or greater than 10 digit")

    @validator("contactPersonPassword")
    def passsowrd_validation(cls, contactPersonPassword):
        if len(contactPersonPassword) == 0:
            raise ValueError("This field should not be empty")
        return contactPersonPassword

    @validator("location")
    def location_validation(cls, location):
        if len(location) == 0:
            raise ValueError("This field should not be empty")
        return location

    @validator("pincode")
    def pincode_validation(cls, pincode):
        if not len(str(pincode)) == 6:
            raise ValueError("This field should not be empty, less or greater than 6 digit")
        return pincode
