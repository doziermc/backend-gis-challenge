import json

import requests


def client():
    """Configure and send POST request to the calculate-properties service.

    Requires the app to be running locally or in docker. Prints the JSON response body
    of the provided GeoJSON feature with appended area, centroid, and bbox properties.
    """
    geojson = {"type":"Feature","properties":{"cats":"delilah"},"geometry":{"coordinates":[[[-105.26033253133266,40.044434356004956],[-105.26033253133266,40.04402520089002],[-105.2596442110887,40.04402520089002],[-105.2596442110887,40.044434356004956],[-105.26033253133266,40.044434356004956]]],"type":"Polygon"}}
    req = requests.post(f"http://127.0.0.1:8000/calculate-properties", json=geojson)
    print(json.dumps(req.json()))


if __name__ == "__main__":
    client()
