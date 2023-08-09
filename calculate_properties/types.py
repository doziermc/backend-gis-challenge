from geojson_pydantic import Feature
from pydantic import BaseModel


class CalcPropRequest(Feature):
    properties: dict


class CalcPropResponseProperties(BaseModel):
    area: float
    centroid: str


class CalcPropResponse(Feature):
    bbox: list[float]
    properties: CalcPropResponseProperties
