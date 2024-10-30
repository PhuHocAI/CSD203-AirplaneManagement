from fastapi import HTTPException
from airport import *
from fastapi import HTTPException
from tortoise.transactions import in_transaction

from typing import List, Dict


################ Add Airport ################
async def add_airport_service(airport: AirportIn_Pydantic): # type: ignore
    airport_obj = await Airport.create(**airport.dict(exclude_unset=True))
    new_airport = await Airport.get(id=airport_obj.id)

    airports = await Airport.all()
    if len(airports) > 1:
        async with in_transaction() as conn:
            for existing_airport in airports:
                if existing_airport.id != new_airport.id:
                    await FlightRoute.create(owner=existing_airport.id, destination=new_airport.name, cost=100, airport=existing_airport)
                    await FlightRoute.create(owner=new_airport.id, destination=existing_airport.name, cost=100, airport=new_airport)
    return new_airport

################ Delete Airport ################
async def delete_airport_service(airport_id: int):
    try:
        airport = await Airport.get(id=airport_id)
        await airport.delete()

        routes = await FlightRoute.all()
        for route in routes:
            if route.owner == airport_id or route.destination == airport.name:
                await route.delete()
        return {
            "status": "Success",
            "message": "Airport deleted successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail="Airport not found")
    

################ Display Airport ################
async def display_airport_service():
    airports = await Airport_Pydantic.from_queryset(Airport.all())
    flight_routes = await FlightRoute_Pydantic.from_queryset(FlightRoute.all())

    responses: Dict[str, List[Dict[str, any]]] = {}
    for airport in airports:
        responses[airport.name] = []
        for route in flight_routes:
            if route.owner == airport.id:
                responses[airport.name].append(route.dict())

    return responses

################ Update Airport ################
async def update_airport_service(airport_id: int, airport: AirportIn_Pydantic):
    try:
        # Lấy thông tin sân bay cần thay đổi
        airport_obj = await Airport.get(id=airport_id)

        # Sửa thông tin sân bay cho các route
        routes = await FlightRoute.all()
        for route in routes:
            if airport.name and route.destination == airport_obj.name:
                route.destination = airport.name
                await route.save()
        
        # câp nhật cost cho các chuyến bay 
        for route in routes:
            if route.owner == airport_id:
                route.cost = 500
                await route.save()

        # Cập nhật lại thông tin mới cho các chuyến bay
        if airport.name:
            airport_obj.name = airport.name
        await airport_obj.save()

        return {
            "status": "Success",
            "message": "Airport updated successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail="Airport not found")


################ Search By Name ################
async def search_airport_by_name_service(name: str):
    airports = await Airport_Pydantic.from_queryset(Airport.filter(name=name))
    if not airports:
        raise HTTPException(status_code=404, detail="Airport not found")
    flight_routes = await FlightRoute_Pydantic.from_queryset(FlightRoute.all())

    responses: Dict[str, List[Dict[str, any]]] = {}
    for airport in airports:
        responses[airport.name] = []
        for route in flight_routes:
            if route.owner == airport.id:
                responses[airport.name].append(route.dict())

    return responses

################ Calculate cost ################
async def calculate_cost_service(airport_des: int, airport_dep: int):
    try:
        airport_des_obj = await Airport.get(id=airport_des)
        routes = await FlightRoute.all()
        for route in routes:
            if route.owner == airport_dep and route.destination == airport_des_obj.name:
                return {
                    "status": "Success",
                    "message": "Cost calculated successfully",
                    "data": route.cost
                }
    except Exception as e:
        raise HTTPException(status_code=404, detail="Airport not found")
