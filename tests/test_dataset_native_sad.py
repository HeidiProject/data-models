import pytest
import json
from pydantic import ValidationError
from pydantic_models.Datasets.native_sad import (
    Model
)

def test_model_1():
    with open('json/Datasets/native-sad', 'r') as file:
        data = json.load(file)
    try:
        Model(**data)
    except ValidationError as e:
        pytest.fail(f"Validation failed with error: {e}")