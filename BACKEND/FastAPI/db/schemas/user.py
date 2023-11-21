def user_schema(user) -> dict:
    return{"id": str(user["_id"]),
           "name": user["name"],
           "corp": user["corp"],
           "capital": user["capital"]}

def users_schema(users) -> list:
    return [user_schema(user) for user in users]
