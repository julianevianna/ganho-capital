from decimal import Decimal

from system.application.enums.operation_type_enum import OperationTypeEnum
from system.domain.entities.base_entity import BaseEntity


class Operation(BaseEntity):
    type: OperationTypeEnum
    unit_cost: Decimal
    quantity: int
