import pytest


@pytest.mark.parametrize(
    "file_name,area,centroid",
    (
        ("polygon.geojson", 2668.62, "POINT (-105.259988 40.044230)"),
        (
            "multipolygon.geojson",
            2864.01,
            "POINT (-105.259361 40.044199)",
        ),
    ),
)
def test_calculate_properties(open_test_json, area, centroid, test_app):
    response = test_app.post("/calculate-properties/", json=open_test_json)

    assert response.status_code == 200
    data = response.json()
    assert data["properties"]["area"] == area
    assert data["properties"]["centroid"] == centroid


@pytest.mark.parametrize("file_name", ["linestring.geojson"])
def test_calculate_properties_wrong_geom(open_test_json, test_app):
    with pytest.raises(ValueError):
        test_app.post("/calculate-properties/", json=open_test_json)
