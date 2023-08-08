import json

import requests


def post_to_service(location: str, body: dict) -> dict:
    """POST request to calculate-properties

    Parameters
    ----------
    location: str
        Location where the app is running: must be docker or local
    body: dict
        JSON request body
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

    Returns
    -------
    dict
        JSON response body of GeoJSON feature with appended properties
    """

    location = "local"  # or docker
    geojson = {"type":"Feature","properties":{},"geometry":{"coordinates":[[[28.713562603965755,3.1970235537500997],[28.644196978193804,3.2064677378855038],[28.6505029441727,3.162394136604817],[28.694644706027702,3.137208378884523],[28.75455138282993,3.118318662109317],[28.757704365819365,3.1875792826630374],[28.748245416851034,3.2316518018622986],[28.713562603965755,3.1970235537500997]]],"type":"Polygon"}}
    req = post_to_service(location, geojson)
    print(json.dumps(req))

if __name__ == "__main__":
    client()
