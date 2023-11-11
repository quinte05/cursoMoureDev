from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   tags=["products"], 
                   responses= {404:{"message": "No encontrado"}})

@router.get("/products")
async def products():
    return "Lista de productos"