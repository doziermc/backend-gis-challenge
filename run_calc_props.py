import json

import requests


def post_to_service(location: str, body: dict) -> dict:
    """
    POST request to calculate-properties

    :param str location: Location where the app is running - docker or local
    :param dict body: GeoJSON feature request body
    :returns: JSON response body from POST request
    """
    if location == "docker":
        addr = "localhost:8000"
    elif location == "local":
        addr = "127.0.0.1:8000"
    else:
        raise ValueError(f"location must be one of docker, local; got {location}")

    req = requests.post(f"http://{addr}/calculate-properties", json=body)
    return req.json()


def client():
    """Configure and send POST request to the calculate-properties service.

    Requires the app to be running locally or in docker. Prints the JSON response body
    of the provided GeoJSON feature with appended area, centroid, and bbox properties.
    """

    location = "local"  # or docker
    geojson =  {"type":"Feature","properties":{"cats":"delilah"},"geometry":{"coordinates":[[[-105.26033253133266,40.044434356004956],[-105.26033253133266,40.04402520089002],[-105.2596442110887,40.04402520089002],[-105.2596442110887,40.044434356004956],[-105.26033253133266,40.044434356004956]]],"type":"Polygon"}}
    req = post_to_service(location, geojson)
    print(json.dumps(req))

if __name__ == "__main__":
    client()
