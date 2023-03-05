from pydantic import BaseModel, EmailStr, validator, Field


class ParameterValidator:
    def validate_name(cls, value):
        if value.startswith(' '):
            raise ValueError("Name can not start with space")
        if value.endswith(' '):
            raise ValueError("Name can not end with space")
        if value.count(' ') > 2:
            raise ValueError("Name must not contain more than Two space")
        if not value.isalpha():
            raise ValueError("Name should be alpha")
        return value

    def validate_age(cls, value):
        for i in value:
            if i.isdigit() and int(i) > 0:
                continue
            else:
                raise ValueError("only digit accepted and value should be greater than zero")
        return value

    def validate_phone_number(cls, value):
        for i in value:
            if i.isdigit():
                continue
            else:
                raise ValueError("Only digit accept")
        return value

    def validate_password(cls, value):
        if len(value) == 0:
            raise ValueError("This field should not be empty")
        return value

    def validate_gender(cls, value):
        for i in value:
            if i.isalpha():
                continue
            else:
                raise ValueError("Enter value properly")
        return value

    def validate_pincode(cls, value):
        for i in value:
            if i.isdigit():
                continue
            else:
                raise ValueError("Only digit accept")
        return value

    def validate_taluka(cls, value):
        for i in value:
            if i.isalpha():
                continue
            else:
                raise ValueError("Check entered value properly")
        return value

    def validate_location(cls, value):
        if len(value) == 0:
            raise ValueError("This field should not be empty")
        return value


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

    _validate_ngo_name = validator('ngoName', allow_reuse=True)(ParameterValidator.validate_name)
    _validate_contact_person_name = validator('contactPersonName', allow_reuse=True)(ParameterValidator.validate_name)
    _validate_phone_number = validator('contactPersonPhone', allow_reuse=True)(ParameterValidator.
                                                                               validate_phone_number)
    _validate_password = validator('contactPersonPassword', allow_reuse=True)(ParameterValidator.validate_password)
    _validate_location = validator('location', allow_reuse=True)(ParameterValidator.validate_location)
    _validate_pincode = validator('pincode', allow_reuse=True)(ParameterValidator.validate_pincode)


class Aanganwadi(BaseModel):
    aanganwadiName: str = Field(..., min_length=2)
    contactPersonName: str = Field(...)
    contactPersonEmail: EmailStr = Field(...)
    contactPersonPhone: str = Field(..., min_length=10, max_length=10)
    contactPersonPassword: str = Field(...)
    taluka: str = Field(...)
    pincode: str = Field(..., min_length=6, max_length=6)

    _validate_aanganwadi_name = validator('aanganwadiName', allow_reuse=True)(ParameterValidator.validate_name)
    _validate_contact_person_name = validator('contactPersonName', allow_reuse=True)(ParameterValidator.validate_name)
    _validate_phone_number = validator('contactPersonPhone', allow_reuse=True)(ParameterValidator.
                                                                               validate_phone_number)
    _validate_password = validator('contactPersonPassword', allow_reuse=True)(ParameterValidator.validate_password)
    _validate_taluka = validator('taluka', allow_reuse=True)(ParameterValidator.validate_taluka)
    _validate_pincode = validator('pincode', allow_reuse=True)(ParameterValidator.validate_pincode)


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

    _validate_chils_name = validator('childName', allow_reuse=True)(ParameterValidator.validate_name)
    _validate_mother_name = validator('motherName', allow_reuse=True)(ParameterValidator.validate_name)
    _validate_child_age = validator('child_age', allow_reuse=True)(ParameterValidator.validate_age)
    _validate_gender = validator('gender', allow_reuse=True)(ParameterValidator.validate_gender)
