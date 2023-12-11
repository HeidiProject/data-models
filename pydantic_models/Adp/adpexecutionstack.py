from pydantic import BaseModel, Field


class AdpExecutionStack(BaseModel):
    field_1: str = Field(..., alias='1')
    field_2: str = Field(..., alias='2')
    field_3: str = Field(..., alias='3')
    field_4: str = Field(..., alias='4')