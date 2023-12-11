import pytest
import json
from pydantic import ValidationError
from pydantic_models.Adp.screening import (
    Model
)

def test_model():
    with open('json/Adp/screening', 'r') as file:
        data = json.load(file)
    try:
        Model(**data)
    except ValidationError as e:
        pytest.fail(f"Validation failed with error: {e}")

