from decimal import Decimal

from system.domain.entities.operation_capital_gain_entity import (
    OperationCapitalGainEntity,
)
from system.domain.value_objects.returns_value_objct import ReturnsValueObject


class SellOperationCapitalGainEntity(OperationCapitalGainEntity):
    returns: ReturnsValueObject
    total_value: Decimal
