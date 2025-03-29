from fastapi import FastAPI
#from app_job.app_job.main import User

app = FastAPI()

#creacion de la ruta de la pagina principal
@app.get("/")
async def root():
    return {"message": "Bienvenidos"}

