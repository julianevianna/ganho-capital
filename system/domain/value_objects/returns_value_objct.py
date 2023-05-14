from decimal import Decimal

from pydantic import root_validator

from system.domain.value_objects.base_value_object import BaseValueObject


class ReturnsValueObject(BaseValueObject):
    average_price: Decimal
    quantity: int
    total_value: Decimal
    previous_loss: Decimal
    returns: Decimal

    @root_validator(pre=True)
    def default_previous_loss(
        cls,
        values,
    ) -> Decimal:
        if "previous_loss" not in values or values["previous_loss"] is None:
            values["previous_loss"] = Decimal("0.00")

        return values

    @root_validator(pre=True)
    def default_returns(cls, values):
        values["returns"] = (
            values["total_value"]
            - values["average_price"] * values["quantity"]
            - values["previous_loss"]
        )

        return values
