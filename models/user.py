from pydantic import BaseModel

class User(BaseModel):
    id: int 
    name: str
    lastname: str
    adress: str

class Company(BaseModel):
    id:int
    name:str
    adress:str
    city:str


