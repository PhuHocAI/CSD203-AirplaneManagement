from fastapi import HTTPException
from airport import *
from fastapi import HTTPException
from tortoise.transactions import in_transaction

from typing import List


################ Add Airport ################

async def add_airport_service(airport: Airport_Pydantic): # type: ignore
    try:
        async with in_transaction():
            airport_obj = await Airport.create(**airport.dict(exclude_unset=True))
            new_airport = await Airport_Pydantic.from_tortoise_orm(airport_obj)
            
            existing_airports = await Airport.all().exclude(id=new_airport.id)

            if len(existing_airports) > 1:
                for existing_airport in existing_airports:
                    await FlightRoute.create(
                        airport_id=new_airport.id,  
                        destination=existing_airport.name,
                        cost=100
                    )
                    await FlightRoute.create(
                        airport_id=existing_airport.id,
                        destination=new_airport.name,
                        cost=100
                    )

            return {
                "status": "success",
                "message": "Airport added successfully",
                "data": {
                    "airport": new_airport.name,
                    "id": new_airport.id,
                }
            }
    except Exception as e:
        print(f"Exception occurred: {e}")
        raise HTTPException(status_code=400, detail=f"Failed to add airport: {str(e)}")

################ Delete Airport ################

async def delete_airport_service(airport_id: int):
    try:
        airport = await Airport.get(id=airport_id)
        
        async with in_transaction():
            # await FlightRoute.filter(airport_id=airport_id).delete()
            # await FlightRoute.filter(destination=airport.name).delete() 
            
            await airport.delete()
        
        return {
            "status": "success",
            "message": "Airport deleted successfully",
            "data": {
                "airport_id": airport_id,
            }
        }

    except Airport.DoesNotExist:
        raise HTTPException(status_code=404, detail="Airport not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete airport: {str(e)}")

################ Show Airport ################

async def get_airports_with_routes_service():
    try:
        airports = await Airport_Pydantic.from_tortoise_orm(Airport.all())
        flights = await FlightRoute_Pydantic.from_queryset(FlightRoute.all())
        return {
            "status": "success",
            "message": "Airports fetched successfully",
            "data": {
                "airports": airports,
                "flights": flights
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


################ Update Airport ################

async def update_airport_service(airport_id: int, updated_data: dict):
    try:
        async with in_transaction():
            airport = await Airport.get(id=airport_id)
            await airport.update_from_dict(updated_data)
            await airport.save()
            return {"status": "success", "message": "Airport updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Airport not found")
    
################ Calculate Route Cost Time ################

async def calculate_route_cost_time(start_airport_id: int, end_airport_id: int):
    # try:
        # route = await FlightRoute.filter(airport_id=start_airport_id, destination=end_airport_id).first()
    #     if route:
    #         return {"status": "success", "cost": route.cost, "time": route.time}
    #     else:
    #         raise HTTPException(status_code=404, detail="Route not found")
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail="Failed to calculate cost and time")
    pass

################ Find Shortest Route ################

async def find_shortest_route(start_airport_id: int, end_airport_id: int):
    pass