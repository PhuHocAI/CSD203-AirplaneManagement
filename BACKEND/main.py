from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from airport import *
from services import *
from pydantic import BaseModel

app = FastAPI()

register_tortoise(
    app,
    db_url="sqlite://database/db.sqlite3",
    modules={"models": ["airport"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.post("/airport/add")
async def add_airport(airport: AirportIn_Pydantic):
    new_airport = await add_airport_service(airport)
    return {
        "message": "Airport added successfully",
        "data": new_airport
    }

@app.delete("/airport/delete/{airport_id}")
async def delete_airport(airport_id: int):
    return await delete_airport_service(airport_id)

@app.get("/airport/display")
async def display_airport():
    responses = await display_airport_service()
    return {
        "message": "List of airports",
        "data": responses
    }

@app.put("/airport/update/{airport_id}")
async def update_airport(airport_id: int, airport: AirportIn_Pydantic):
    return await update_airport_service(airport_id, airport)

@app.get("/airport/search_by_name/{airport_name}")
async def search_airport_by_name(airport_name: str):
    return await search_airport_by_name_service(airport_name)

@app.get("/airport/calculate_cost/{airport_des}/{airport_dep}")
async def calculate_cost(airport_des: int, airport_dep: int):
    return await calculate_cost_service(airport_dep, airport_des)