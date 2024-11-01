from pydantic import BaseModel
from tortoise import fields, Model
from tortoise.contrib.pydantic import pydantic_model_creator
import datetime
from typing import Dict, List


class Airport(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=50, unique=True, null=False)

class FlightRoute(Model):
    id = fields.IntField(pk=True)
    owner = fields.IntField(null=False)
    destination = fields.CharField(max_length=50, null=False)
    cost = fields.FloatField()
    airport = fields.ForeignKeyField('models.Airport', related_name='routes')

Airport_Pydantic = pydantic_model_creator(Airport, name="Airport",)
AirportIn_Pydantic = pydantic_model_creator(Airport, name="AirportIn", exclude_readonly=True)
AirportWithRoutes_Pydantic = pydantic_model_creator(
    Airport, name="AirportWithRoutes", include=("id", "name", "routes")
)


FlightRoute_Pydantic = pydantic_model_creator(
    FlightRoute, name="FlightRoute", include=("id", "destination", "cost", "owner")
)
FlightRouteIn_Pydantic = pydantic_model_creator(FlightRoute, name="FlightRouteIn", exclude_readonly=True)
