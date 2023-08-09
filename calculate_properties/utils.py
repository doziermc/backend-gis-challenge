import math
import typing

import shapely
import shapely.wkt
from pyproj import Geod
from shapely.geometry import MultiPolygon, Polygon


def calculate_centroid(geom: typing.Union[Polygon, MultiPolygon]) -> str:
    """
    Get the centroid of a shapely geometry

    :param shapely.geometry geom: shapely polygon or multipolygon
    :returns: wkt of centroid POINT
    """
    print(type(geom))
    centroid = geom.centroid
    return shapely.wkt.dumps(centroid, rounding_precision=6)


def calculate_area_sqm(geom: typing.Union[Polygon, MultiPolygon]) -> float:
    """
    Calculate the geodesic area in m2 of a shapely geometry.
    Requires geographic coordinates.

    :param shapely.geometry geom: shapely polygon or multipolygon
    :returns: area of geometry in square meters
    :raises ValueError: area calculation fails on non-geographic data
    """

    # specify ellipsoid
    geod = Geod(ellps="WGS84")
    poly_area, _ = geod.geometry_area_perimeter(geom)
    if math.isnan(poly_area):
        raise ValueError("Cannot calculate area. Is your feature in a geographic CRS?")
    return round(poly_area, 2)


def calculate_bbox(geom: typing.Union[Polygon, MultiPolygon]) -> list[float]:
    """return the bbox of a shapely geometry as an array of minx, miny, maxx, maxy

    :param shapely.geometry geom: shapely polygon or multipolygon
    :returns: bbox array
    """
    bounds = geom.bounds
    bbox_prec = [(round(i, 6)) for i in bounds]
    return bbox_prec
