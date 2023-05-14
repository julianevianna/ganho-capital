from decimal import Decimal
from typing import List

from system.domain.entities.base_entity import BaseEntity
from system.domain.entities.operation_capital_gain_entity import \
    OperationCapitalGainEntity


class OperationListEntity(BaseEntity):
    operations: List[OperationCapitalGainEntity]
    tax_rate: Decimal
    weighted_average_price: Decimal
