import pytest
from shapely.geometry import shape

from calculate_properties.utils import (calculate_area_sqm, calculate_bbox,
                                        calculate_centroid)


@pytest.mark.parametrize(
    "file_name,expected",
    (
        ("polygon.geojson", 2668.62),
        ("multipolygon_holes.geojson", 501943778116.14),
        ("multipolygon.geojson", 2864.01),
    ),
)
def test_calculate_area_sqm(open_test_json, expected):
    area = calculate_area_sqm(shape(open_test_json["geometry"]))
    assert area == expected


@pytest.mark.parametrize(
    "file_name,expected",
    (
        ("polygon.geojson", [-105.260333, 40.044025, -105.259644, 40.044434]),
        ("multipolygon_holes.geojson", [-51.591797, -21.309846, -41.11084, -14.944785]),
        ("multipolygon.geojson", [-105.260811, 40.043599, -105.260451, 40.043852]),
    ),
)
def test_calculate_bbox(open_test_json, expected):
    bbox = calculate_bbox(shape(open_test_json["geometry"]))
    assert bbox == expected


@pytest.mark.parametrize(
    "file_name,expected",
    (
        ("polygon.geojson", "POINT (-105.259988 40.044230)"),
        ("multipolygon_holes.geojson", "POINT (-46.137702 -18.244096)"),
        ("multipolygon.geojson", "POINT (-105.259361 40.044199)"),
    ),
)
def test_calculate_centroid(open_test_json, expected):
    centroid_str = calculate_centroid(shape(open_test_json["geometry"]))
    assert centroid_str == expected
