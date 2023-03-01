from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    username: str
    password: str
    user_type: str


class Ngo(BaseModel):
    ngoName: str
    contactPersonName: str
    contactPersonEmail: EmailStr
    contactPersonPhone: str
    contactPersonPassword: str
    location: str
    pincode: str

    @validator("ngoName")
    def val(cls, ngoName):
        for i in ngoName:
            if i.isalpha():
                continue
            elif i == ' ':
                continue
            else:
                raise ValueError("not accepted")
        return ngoName

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
        if not len(contactPersonPhone) == 10:
            raise ValueError(
                "This field should not be empty, and should not be less or greater than 10 digit")
        return contactPersonPhone

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
        if not len(pincode) == 6:
            raise ValueError(
                "This field should not be empty, less or greater than 6 digit")
        return pincode


class Aanganwadi(BaseModel):
    aanganwadiName: str
    contactPersonName: str
    contactPersonEmail: EmailStr
    contactPersonPhone: int
    contactPersonPassword: str
    taluka: str
    pincode: int


class Donor(BaseModel):
    name: str
    contactperson: str
    email: EmailStr
    phone: int


class Child(BaseModel):
    childName: str
    motherName: str
    child_age: str
    gender: str
    isActive: bool
