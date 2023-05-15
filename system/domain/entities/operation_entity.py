from decimal import Decimal

from pydantic import Field

from system.application.enums.operation_type_enum import OperationTypeEnum
from system.domain.entities.base_entity import BaseEntity


class OperationEntity(BaseEntity):
    type: OperationTypeEnum = Field(..., alias="operation")
    unit_cost: Decimal
    quantity: int
