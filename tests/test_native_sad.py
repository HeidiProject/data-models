import pytest
import json
from pydantic import ValidationError
from pydantic_models.Adp.native_sad import (
    Model
)

def test_model_1():
    with open('json/Adp/native-sad-1-of-3', 'r') as file:
        data = json.load(file)
    try:
        Model(**data)
    except ValidationError as e:
        pytest.fail(f"Validation failed with error: {e}")

def test_model_2():
    with open('json/Adp/native-sad-2-of-3', 'r') as file:
        data = json.load(file)
    try:
        Model(**data)
    except ValidationError as e:
        pytest.fail(f"Validation failed with error: {e}")

def test_model_3():
    with open('json/Adp/native-sad-3-of-3', 'r') as file:
        data = json.load(file)
    try:
        Model(**data)
    except ValidationError as e:
        pytest.fail(f"Validation failed with error: {e}")