from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    occupation: str
    address: str

class Success(BaseModel):
    success: bool
    result: dict

app = FastAPI()

data = []

@app.get("/person")
async def get_person():
    person_x = []
    for element in data:
        persons = element
        person_x.append(persons)
    return {"Database" : person_x}

@app.post("/person", response_model=Success)
async def create_person(person_request: Person):
        
        if (person_request.name.strip() == "" 
        or person_request.occupation.strip() == ""
        or person_request.address.strip() == ""):
            return {"success" : False, 
                   "result" : {"error_message" : "invalid request"}}
    
        data_json = jsonable_encoder(person_request)
        data.append(data_json)
        return {"success" : True,
            "result" : data_json}

