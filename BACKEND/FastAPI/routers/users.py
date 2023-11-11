from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    surname: str
    capital: str
    
users_list = [User(id= 0, name= "andres", surname= "Quintero", capital= "100k"),
              User(id= 1, name= "felipe", surname= "Gutierrez", capital= "100k"),
              User(id= 2, name= "rafa", surname= "moncada", capital= "100k")]

@router.get("/usersjson")
async def usersjson():
    return [{"name": "andres", "surname": "Quintero", "capital": "100k"},
            {"name": "felipe", "surname": "Gutierrez", "capital": "100k"}]

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")
async def user(id: int):
    return search_id(id)

@router.get("/user/")
async def user(id: int):
    return search_id(id)

@router.post("/user/", status_code=201)
async def user(user : User):
    if type(search_id(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user
        
@router.put("/user/")
async def user(user : User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user
        
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
        if not found:
            return {"error": "No se ha eliminado el usuario"}
        else:
            return {"error": "Se ha eliminado el usuario correctamente"}
    
def search_id(id: int): 
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "Usuario no encontrado"
    