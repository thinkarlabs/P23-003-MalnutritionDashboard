from pydantic import BaseModel, EmailStr, validator, Field


class User(BaseModel):
    username: str
    password: str
    user_type: str


class Ngo(BaseModel):
    ngoName: str = Field(...)
    contactPersonName: str = Field(...)
    contactPersonEmail: EmailStr = Field(...)
    contactPersonPhone: str = Field(..., min_length=10, max_length=10)
    contactPersonPassword: str = Field(...)
    location: str = Field(...)
    pincode: str = Field(..., min_length=6, max_length=6)

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
        for i in contactPersonPhone:
            if i.isdigit():
                continue
            else:
                raise ValueError("Only digit accept")
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
        for i in pincode:
            if i.isdigit():
                continue
            else:
                raise ValueError("Only digit accept")
        return pincode


class Aanganwadi(BaseModel):
    aanganwadiName: str = Field(..., min_length=2)
    contactPersonName: str = Field(...)
    contactPersonEmail: EmailStr = Field(...)
    contactPersonPhone: str = Field(..., min_length=10, max_length=10)
    contactPersonPassword: str = Field(...)
    taluka: str = Field(...)
    pincode: str = Field(..., min_length=6, max_length=6)

    @validator("aanganwadiName")
    def val(cls, aanganwadiName):
        for i in aanganwadiName:
            if i.isalpha():
                continue
            elif i == ' ':
                continue
            else:
                raise ValueError("not accepted")
        return aanganwadiName

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
        for i in contactPersonPhone:
            if i.isdigit():
                continue
            else:
                raise ValueError("Only digit accept")
        return contactPersonPhone

    @validator("taluka")
    def taluka_validation(cls, taluka):
        for i in taluka:
            if i.isalpha():
                continue
            else:
                raise ValueError("Check entered value properly")
        return taluka

    @validator("pincode")
    def pincode_validation(cls, pincode):
        for i in pincode:
            if i.isdigit():
                continue
            else:
                raise ValueError("Only digit accept")
        return pincode


class Donor(BaseModel):
    name: str
    contactperson: str
    email: EmailStr
    phone: int


class Child(BaseModel):
    childName: str
    motherName: str
    child_age: str = Field(..., min_length=1, max_length=2)
    gender: str
    isActive: bool

    @validator("childName")
    def child_name_validation(cls, childName):
        for i in childName:
            if i.isalpha():
                continue
            elif i == ' ':
                continue
            else:
                raise ValueError("not accepted")
        return childName

    @validator("motherName")
    def mother_name_validation(cls, motherName):
        for i in motherName:
            if i.isalpha():
                continue
            elif i == ' ':
                continue
            else:
                raise ValueError("not accepted")
        return motherName

    @validator("child_age")
    def child_age_validation(cls, child_age):
        for i in child_age:
            if i.isdigit() and int(i) > 0:
                continue
            else:
                raise ValueError("only digit accepted and value should be greater than zero")

    @validator("gender")
    def gender_validation(cls, gender):
        for i in gender:
            if i.isalpha():
                continue
            else:
                raise ValueError("Enter value properly")
