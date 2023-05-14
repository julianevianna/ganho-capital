from decimal import Decimal
from typing import List

from pydantic import BaseModel

from system.application.dto.input import Input
from system.application.enums.operation_type_enum import OperationTypeEnum


class OperationInput(BaseModel):
    operation: OperationTypeEnum
    unit_cost: Decimal
    quantity: int


class OperationsListInput(Input):
    operation_list: List[OperationInput]
