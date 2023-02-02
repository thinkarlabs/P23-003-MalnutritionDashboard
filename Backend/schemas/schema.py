def ngo_serializer(newNgo) -> dict:
    return {
        "id": str(newNgo["_id"]),
        "name": str(newNgo["name"]),
        "email": str(newNgo["email"]),
        "password": str(newNgo["email"]),
        "location": str(newNgo["location"]),
        "pincode": int(newNgo["pincode"])
    }


def ngo_addition_serializer(ngos) -> list:
    return [ngo_serializer(newNgo) for newNgo in ngos]
