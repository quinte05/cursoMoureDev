from fastapi import FastAPI
from routers import products, users

app = FastAPI()

#Routers
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hola Mundo, voy a comerte!"

@app.get("/url")
async def url():
    return "Este es el GET con URL!"

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C
# Url local: http://127.0.0.1:8000

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc