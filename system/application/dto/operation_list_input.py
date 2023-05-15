from decimal import ROUND_HALF_UP, Decimal
from typing import List

from pydantic import Field, validator

from system.application.dto.input import Input
from system.application.enums.operation_type_enum import OperationTypeEnum


class OperationInput(Input):
    operation: OperationTypeEnum
    unit_cost: Decimal = Field(..., alias="unit-cost", ge=Decimal("0.00"))  # type: ignore
    quantity: int = Field(..., ge=0)

    @validator("unit_cost", pre=True)
    def check_unit_cost(cls, v):
        if isinstance(v, float):
            v = Decimal(str(v))
        return (
            Decimal(v).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
            if isinstance(v, Decimal)
            else v
        )

    @validator("operation", pre=True)
    def lowercase_field(cls, v):
        return v.lower() if isinstance(v, str) else v


class OperationsListInput(Input):
    operation_list: List[OperationInput]
