import json
import os

import pytest
from starlette.testclient import TestClient

from calculate_properties.main import app


@pytest.fixture()
def test_app():
    client = TestClient(app)
    return client


@pytest.fixture()
def open_test_json(file_name):
    test_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    file_path = os.path.join(test_data_dir, file_name)
    with open(file_path, "r") as f:
        data = json.load(f)
    return data
