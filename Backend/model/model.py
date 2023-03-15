from datetime import datetime
from pydantic import BaseModel, EmailStr, validator, Field
from bson import ObjectId
from typing import Optional


class ParameterValidator:
    """
    This class created for parameter validation which is passed in model.
    """

    def validate_name(cls, value):

        """
        This function is created for validate the name field.
        :param value: taking value or parameter name from model classes
        :return: After validating the parameter it returns the value(name)
        """
        if value.startswith(' '):
            raise ValueError("Name can not start with space")
        if value.endswith(' '):
            raise ValueError("Name can not end with space")
        if value.count(' ') > 2:
            raise ValueError("Name must not contain more than Two space")
        for i in value:
            if i == " " or i.isalpha():
                continue
        return value

    def validate_age(cls, value):

        """
        This function is created for validate the age field.
        :param value: taking value or parameter name from model classes
        :return: After validating the parameter it returns the value(age)
        """
        for i in value:
            if i.isdigit() and int(i) > 0:
                continue
            else:
                raise ValueError("only digit accepted and value should be greater than zero")
        return value

    def validate_is_digit(cls, value):

        """
        This function is created for validate the pincode, phone number field and the parameter which contain digit
        value.
        :param value: taking value or parameter name from model classes
        :return: After validating the parameter it returns the value(pincode or phone-number)
        """
        if not value.isdigit():
            raise ValueError("Value should be digit")
        return value

    def validate_is_empty(cls, value):

        """
        This function is created for validate the field value is it present or not.
        :param value: taking value or parameter name from model classes
        :return: After validating the parameter it returns the value
        """
        if len(value) == 0:
            raise ValueError("This field should not be empty")
        return value

    def validate_is_alpha(cls, value):

        """
        This function is created for validate the field which value should be alphabet.
        :param value:
        :return:
        """
        if not value.isalpha():
            raise ValueError("Value should be alphabet")
        return value


class User(BaseModel):
    username: str
    password: str
    user_type: str


class Ngo(BaseModel):
    """
    This Ngo class has created for storing the required Ngo field value in database.
    """
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
                                                                               validate_is_digit)
    _validate_password = validator('contactPersonPassword', allow_reuse=True)(ParameterValidator.validate_is_empty)
    _validate_location = validator('location', allow_reuse=True)(ParameterValidator.validate_is_empty)
    _validate_pincode = validator('pincode', allow_reuse=True)(ParameterValidator.validate_is_digit)


class Aanganwadi(BaseModel):
    """
    This Aanganwadi class has created for storing the required Aanganwadi field value in database.
    """
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
                                                                               validate_is_digit)
    _validate_password = validator('contactPersonPassword', allow_reuse=True)(ParameterValidator.validate_is_empty)
    _validate_taluka = validator('taluka', allow_reuse=True)(ParameterValidator.validate_is_empty)
    _validate_pincode = validator('pincode', allow_reuse=True)(ParameterValidator.validate_is_digit)


class Donor(BaseModel):
    """
    This Donor class has created for storing the required Donor field value in database.
    """
    name: str
    contactperson: str
    email: EmailStr
    phone: int


class Child(BaseModel):
    """
    This Child class has created for storing the required Child field value in database.
    """
    childName: str
    motherName: str
    child_age: str = Field(..., min_length=1, max_length=2)
    gender: str
    isActive: bool

    _validate_child_name = validator('childName', allow_reuse=True)(ParameterValidator.validate_name)
    _validate_mother_name = validator('motherName', allow_reuse=True)(ParameterValidator.validate_name)
    _validate_child_age = validator('child_age', allow_reuse=True)(ParameterValidator.validate_age)
    _validate_gender = validator('gender', allow_reuse=True)(ParameterValidator.validate_is_alpha)


class ChildMalnutrition(BaseModel):
    """
    This ChildMalnutrition class has created for storing the required ChildMalnutrition field value in database.
    """
    date: datetime
    malnutritionIndexCategory: str
    height: float
    weight: float
    child_id: str


class Supplementary(BaseModel):
    """
    This Supplementary class has created for storing the required Supplementary field value in database.
    """
    id: Optional[str] = Field(str(ObjectId()), alias="_id")
    original_id: str
    given_date: str
    no_of_packs_given: int
    supplementary_id: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class SupplementsDetail(BaseModel):

    """
    This SupplementsDetail class has created for store the details about supplements in DB.
    """
    name: str = Field(...)
    description: str

class Donor(BaseModel):
    id: str = Field(alias="_id")
    name: str

    class Config:
        orm_mode = True


class Supplement(BaseModel):
    id: str = Field(alias="_id")
    name: str

    class Config:
        orm_mode = True


class Program(BaseModel):
    id: str = Field(alias="_id")
    code: str
    donor: Donor
    supplement: Supplement
    from_date: datetime
    to_date: datetime
    notes: Optional[str] = None

    class Config:
        orm_mode = True

