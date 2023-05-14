from decimal import Decimal

from system.domain.entities.operation_capital_gain_entity import \
    OperationCapitalGainEntity
from system.domain.value_objects.returns_value_objct import ReturnsValueObject
from system.domain.value_objects.tax_value_object import TaxValueObject


class SellOperationCapitalGainEntity(OperationCapitalGainEntity):
    returns: ReturnsValueObject
    tax: TaxValueObject
    total_value: Decimal
