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
        "contactPersonPhone": int(newNgo["contactPersonPhone"]),
        "location": str(newNgo["location"]),
        "pincode": int(newNgo["pincode"])
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
        "aanganwadiName": str(newAanganwadi["aanganwadiName"]),
        "contactPersonName": str(newAanganwadi["contactPersonName"]),
        "contactPersonEmail": str(newAanganwadi["contactPersonEmail"]),
        "contactPersonPassword": str(newAanganwadi["contactPersonPassword"]),
        "contactPersonPhone": int(newAanganwadi["contactPersonPhone"]),
        "taluka": str(newAanganwadi["taluka"]),
        "pincode": int(newAanganwadi["pincode"])
    }


def aanganwadi_list_serializer(aanganwadis) -> list:
    return [aanganwadi_serializer(aanganwadi) for aanganwadi in aanganwadis]
