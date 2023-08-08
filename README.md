## Calculate Properties
A FastAPI-based REST application that accepts a Polygon/Multipolygon GeoJSON feature and returns the feature with: 

- new properties: area (sqm) and centroid (wkt)
- bbox array

## Usage
The calculate properties app can be run locally or in a docker container.

Prerequisites:
- python 3.10 installed and set as your active python version
- `virtualenv` and `requests` installed
- docker installed, if running containerized version

### local usage
1. Create and activate a new python 3.10 virtualenv:
```bash
python -m venv env
source env/bin/activate
```

2. Install project dependencies:
```bash
pip install -r requirements.txt
```

3. To run tests, run:
```bash
pytest -s --cov
```

4. Start the server:
```bash
uvicorn calculate_properties.main:app --reload
```

5. Open `run_calc_props.py` and ensure the `location` variable is set to "local". Update the `geojson` variable to one of your choosing, and run the script in a new terminal: 

```bash
backend-gis-challenge % python run_calc_props.py
{"bbox": [-105.260333, 40.044025, -105.259644, 40.044434], "type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[-105.26033253133266, 40.044434356004956], [-105.26033253133266, 40.04402520089002], [-105.2596442110887, 40.04402520089002], [-105.2596442110887, 40.044434356004956], [-105.26033253133266, 40.044434356004956]]]}, "properties": {"area": 2668.62, "centroid": "POINT (-105.259988 40.044230)"}}
```

### docker usage
Use the makefile to run the app in docker. 

1. run tests: 
```bash
make docker-test
```

2. Run the app from the docker container: 
```bash
make docker-run
```

3. Open `run_calc_props.py` and ensure the `location` variable is set to "docker". Update the `geojson` variable to one of your choosing, and run the script in a new terminal: 


## Assumptions and design decisions
1. Property over-writes. Pre-existing GeoJSON properties, if any, will be removed by the pydantic model when run through this app. While this app version standardizes GeoJSON input to the output type, typing could be relaxed if this is not the intent of the service.

2. The app assumes that incoming features have a properties dict, even if it is empty. 

3. Coordinate precision. I rounded centroid and bbox precision to 6 decimal places, based on [these considerations](https://datatracker.ietf.org/doc/html/rfc7946#section-11.2). 

3. Synchronous processing. I considered whether the `calculate-properties` endpoint should be `async` and decided that it was not necessary, since the libraries used are not being awaited or using long I/O operations, and because FastAPI natively [uses an external threadpool](https://fastapi.tiangolo.com/async/#path-operation-functions).

4. Dependency management. Dependencies are managed using `pip-tools` and `pip-compile` as a lightweight dependency management system that contains a record of working pinned versions. I didn't think it was necessary to split dev and prod dependencies for this effort. 
