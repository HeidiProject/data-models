#  Create python tests to pass the json data into a standard gopy pydantic model

import pytest
import json
from pydantic import ValidationError
from pydantic_models.Adp.standard_autoproc import (
    Model
)

def test_model():
    with open('json/Adp/standard-autoproc', 'r') as file:
        data = json.load(file)
    try:
        Model(**data)
    except ValidationError as e:
        pytest.fail(f"Validation failed with error: {e}")

