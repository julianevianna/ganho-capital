from decimal import Decimal

from pydantic import root_validator

from system.domain.value_objects.base_value_object import BaseValueObject


class ReturnsValueObject(BaseValueObject):
    average_price: Decimal
    quantity: int
    total_value: Decimal
    returns: Decimal

    @root_validator(pre=True)
    def default_returns(cls, values):
        values["returns"] = (
            values["total_value"] - values["average_price"] * values["quantity"]
        )

        return values
