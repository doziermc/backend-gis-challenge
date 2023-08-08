from fastapi import FastAPI
from shapely.geometry import shape

from calculate_properties.types import (CalcPropRequest, CalcPropResponse,
                                        CalcPropResponseProperties)
from calculate_properties.utils import (calculate_area_sqm, calculate_bbox,
                                        calculate_centroid)

app = FastAPI()


@app.post("/calculate-properties/")
def calculate_properties(request_data: CalcPropRequest) -> CalcPropResponse:
    """Adds centroid and area (sqm) properties and bbox to GeoJSON feature."""
    shp = shape(request_data.geometry)

    # validate geom type
    if shp.geom_type not in ("MultiPolygon", "Polygon"):
        raise ValueError(
            f"feature must be one of MultiPolygon, Polygon, got {shp.geom_type}"
        )

    # calculate centroid, bbox, and area
    centroid = calculate_centroid(shp)
    bbox = calculate_bbox(shp)
    area_sqm = calculate_area_sqm(shp)

    # type check properties
    properties = CalcPropResponseProperties(area_sqm=area_sqm, centroid=centroid)

    return CalcPropResponse(
        bbox=bbox, type="Feature", geometry=request_data.geometry, properties=properties
    )
