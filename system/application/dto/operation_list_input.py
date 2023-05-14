from decimal import Decimal
from typing import List

from pydantic import Field

from system.application.dto.input import Input
from system.application.enums.operation_type_enum import OperationTypeEnum


class OperationInput(Input):
    operation: OperationTypeEnum
    unit_cost: Decimal = Field(..., alias="unit-cost")
    quantity: int


class OperationsListInput(Input):
    operation_list: List[OperationInput]
