def user_serializer(newUser) -> dict:
    return {
        "id": str(newUser["_id"]),
        "username": str(newUser["username"]),
        "password": str(newUser["password"]),
        "user_type": str(newUser["user_type"])
    }


def user_list_serializer(users) -> list:
    return [user_serializer(newUser) for newUser in users]


def ngo_serializer(newNgo) -> dict:
    return {
        "id": str(newNgo["_id"]),
        "ngoName": str(newNgo["ngoName"]),
        "contactPersonName": str(newNgo["contactPersonName"]),
        "contactPersonEmail": str(newNgo["contactPersonEmail"]),
        "contactPersonPassword": str(newNgo["contactPersonPassword"]),
        "contactPersonPhone": str(newNgo["contactPersonPhone"]),
        "location": str(newNgo["location"]),
        "pincode": str(newNgo["pincode"])
    }


def ngo_list_serializer(ngos) -> list:
    return [ngo_serializer(ngo) for ngo in ngos]


def donor_serializer(newdonor) -> dict:
    return {
        "id": str(newdonor["_id"]),
        "name": str(newdonor["name"]),
        "contactperson": str(newdonor["contactperson"]),
        "email": str(newdonor["email"]),
        "phone": int(newdonor["phone"])
    }


def donors_list_serializer(donors) -> list:
    return [donor_serializer(donor) for donor in donors]


def aanganwadi_serializer(newAanganwadi) -> dict:
    return {
        "id": str(newAanganwadi["_id"]),
        "contactPersonName": str(newAanganwadi["contactPersonName"]),
        "contactPersonPassword": str(newAanganwadi["contactPersonPassword"]),
        "contactPersonPhone": str(newAanganwadi["contactPersonPhone"]),
        "location_coordinates": str(newAanganwadi["location_coordinates"]),
        "location": str(newAanganwadi["location"])
    }


def aanganwadi_list_serializer(aanganwadis) -> list:
    return [aanganwadi_serializer(aanganwadi) for aanganwadi in aanganwadis]


def child_serializer(newChild) -> dict:
    return {
        "id": str(newChild["_id"]),
        "childName": str(newChild["childName"]),
        "motherName": str(newChild["motherName"]),
        "child_age": str(newChild["child_age"]),
        "gender": str(newChild["gender"]),
        "isActive": bool(newChild["isActive"])
    }


def child_list_serializer(childs) -> list:
    return [child_serializer(child) for child in childs]


def child_malnutrition_serializer(childMalnutrition) -> dict:
    return {
        "id": str(childMalnutrition["_id"]),
        "date": str(childMalnutrition["date"]),
        "malnutritionIndexCategory": str(childMalnutrition["malnutritionIndexCategory"]),
        "height": str(childMalnutrition["height"]),
        "weight": str(childMalnutrition["weight"]),
        "child_id": str(childMalnutrition["child_id"])
    }


def child_malnutrition_list_serializer(childsMalnutrition) -> list:
    return [child_malnutrition_serializer(child) for child in childsMalnutrition]


def supplementaryPacks_serializer(supplementarypack) -> dict:
    return {
        "id": str(supplementarypack["_id"]),
        "program_joining_id": str(supplementarypack["program_joining_id"]),
        "given_date": str(supplementarypack["given_date"]),
        "no_of_packs_given": int(supplementarypack["no_of_packs_given"])
    }


def supplementaryPacks_list_serializer(supplementarypacks) -> list:
    return [supplementaryPacks_serializer(packs) for packs in supplementarypacks]


def supplement_serializer(supplement) -> dict:
    return {
        "id": str(supplement["_id"]),
        "name": str(supplement["name"]),
        "description": str(supplement["description"])
    }


def supplements_list_serializer(supplements) -> list:
    return [supplement_serializer(supplementary) for supplementary in supplements]


def program_serializer(program) -> dict:
    return {
        "id": str(program["_id"]),
        "title": str(program["title"]),
        "invite_code": str(program["invite_code"]),
        "donor_id": str(program["donor_id"]),
        "donor_name": str(program["donor_name"]),
        "supplements_details_id": str(program["supplements_details_id"]),
        "supplement_name": str(program["supplement_name"]),
        "from_date": str(program["from_date"]),
        "to_date": str(program["to_date"]),
        "notes": str(program["notes"])
    }


def program_list_serializer(programs) -> list:
    return [program_serializer(programs_list) for programs_list in programs]


def programjoining_serializer(program_joining) -> dict:
    return {
        "id": str(program_joining["_id"]),
        "invite_code": str(program_joining["invite_code"]),
        "aanganwadi_id": str(program_joining["aanganwadi_id"]),
        "program_id": str(program_joining["program_id"]),
        "isActive": bool(program_joining["isActive"]),
    }


def programjoining_list_serializer(programs_joining) -> list:
    return [programjoining_serializer(programs) for programs in programs_joining]
