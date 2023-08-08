import typing

import shapely
import shapely.wkt
from pyproj import Geod
from shapely.geometry import MultiPolygon, Polygon


def calculate_centroid(geom: typing.Union[Polygon, MultiPolygon]) -> str:
    """return the centroid of a shapely polygon or multipolygon as wkt"""
    centroid = geom.centroid
    return shapely.wkt.dumps(centroid, rounding_precision=6)


def calculate_area_sqm(geom: typing.Union[Polygon, MultiPolygon]) -> float:
    """return the area in m2 of a shapely polygon or multipolygon"""
    geod = Geod(ellps="WGS84")
    poly_area, _ = geod.geometry_area_perimeter(geom)
    return round(poly_area, 2)


def calculate_bbox(geom: typing.Union[Polygon, MultiPolygon]) -> list[float]:
    """return the bbox of a shapely polygon or multipolygon as an array of
    minx, miny, maxx, maxy
    """
    bounds = geom.bounds
    bbox_prec = [(round(i, 6)) for i in bounds]
    return bbox_prec
