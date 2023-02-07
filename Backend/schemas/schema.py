

def user_serializer(newUser) -> dict:
    return {
        "id": str(newUser["_id"]),
        "username": str(newUser["username"]),
        "password": str(newUser["password"]),
        "user_type": str(newUser["user_type"]
    }
def user_list_serializer(users) -> list:
    return [user_serializer(newUser) for newUser in users]



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

