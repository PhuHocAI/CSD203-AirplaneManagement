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

@app.get("/")
async def root():
    return {"message": "Welcome to the Airport Management System with Tortoise ORM!"}

############ Add Airport ############

@app.post("/airport/add_airport")
async def add_airport(airport: Airport_Pydantic):  # type: ignore
    response = await add_airport_service(airport)
    return response

############ Delete Airport ############

@app.delete("/airport/delete_airport/{airport_id}")
async def delete_airport(airport_id: int):
    response = await delete_airport_service(airport_id)
    return response

############ Display Airports ############

@app.get("/airports_with_routes", response_model=List[AirportWithRoutes_Pydantic])
async def get_airports_with_routes():
    response = await get_airports_with_routes_service()
    return response

############ Update Airport ############
@app.put("/airport/update_airport/{airport_id}")
async def update_airport(airport_id: int, airport_data: dict):
    response = await update_airport_service(airport_id, airport_data)
    return response


############ Calculate Route Cost Time ############
@app.get("/airport/calculate_route_cost_time")
async def get_route_cost_time(start_airport_id: int, end_airport_id: int):
    response = await calculate_route_cost_time(start_airport_id, end_airport_id)
    return response

############ Find Shortest Route ############
@app.get("/airport/find_shortest_route")
async def shortest_route(start_airport_id: int, end_airport_id: int):
    response = await find_shortest_route(start_airport_id, end_airport_id)
    return response