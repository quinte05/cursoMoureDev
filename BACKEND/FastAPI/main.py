from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola Mundo, voy a comerte!"

@app.get("/url")
async def url():
    return "Este es el GET con URL!"

