# Backend GIS Challenge
A simple coding challenge for Geospatial backend development using GeoJSON

- https://geojson.org/

## Requirements

Write a backend REST application with a single POST endpoint `/calculate_properties` to calculate Geojson Feature properties and return them to the user.  

- Accept a plain Geojson Feature (Polygon or Multipolygon).
- Return it back to the user with `properties` and `bbox` added, following GeoJSON standards for response format.
- The following `properties` should be included in the response:
  - `area` in sq meters
  - `centroid`
- Python 3.10+ must be used.
- Instructions should be provided for an evaluator to:
  - Run the app locally and exercise the endpoint.
  - Run any automated tests locally.
- Code should be in a git-clonable repo.

## How the challenge will be evaluated
- Code will be subjectively evaluated as per a normal Code Review for quality.
- Simple, valid requests should work locally.
- Automated tests should run locally and pass.
- Do not focus on edge cases or handling invalid inputs.
- Write code that you feel is production-quality in terms of 
  - Cleanliness
  - Organization
  - Automated Testing
  
**Suggested completion time is 1-4 hours.**
