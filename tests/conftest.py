
import os
import pickle

import pytest
from fastapi.testclient import TestClient

import ris


TEST_DIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(TEST_DIR, "data", "iris_validation_classes.pkl"), "rb") as f:
    validation_classes = pickle.load(f)


with open(os.path.join(TEST_DIR, "data", "iris_validation_features.pkl"), "rb") as f:
    validation_features = pickle.load(f)


@pytest.fixture
def test_client():
    return TestClient(ris.api.app)


@pytest.fixture(
    params=zip(validation_classes, validation_features)
)
def iris_test_data(request):
    return {
        "class": request.param[0],
        "features": request.param[1]
    }


@pytest.fixture
def all_validation_classes():
    return validation_classes


@pytest.fixture
def all_validation_features():
    return validation_features


@pytest.fixture
def all_validation(all_validation_classes, all_validation_features):
    return zip(all_validation_classes, all_validation_features)
