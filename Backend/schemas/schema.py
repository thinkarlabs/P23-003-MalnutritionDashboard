def user_serializer(newUser) -> dict:
    return {
        "id": str(newUser["_id"]),
        "username": str(newUser["username"]),
        "password": str(newUser["password"]),
        "user_type": str(newUser["user_type"])

    }


def user_addition_serializer(users) -> list:
    return [user_serializer(newUser) for newUser in users]
