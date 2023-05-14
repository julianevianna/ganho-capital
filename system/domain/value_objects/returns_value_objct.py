from decimal import Decimal
from typing import Optional

from system.domain.value_objects.base_value_object import BaseValueObject


class ReturnsValueObject(BaseValueObject):
    average_price: Decimal
    quantity: Decimal
    total_value: Decimal
    loss: Optional[Decimal]
    returns: Decimal
