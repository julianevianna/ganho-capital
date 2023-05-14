from decimal import Decimal

from pydantic import root_validator, validator

from system.application.enums.operation_type_enum import OperationTypeEnum
from system.domain.entities.operation_capital_gain_entity import (
    OperationCapitalGainEntity,
)
from system.domain.value_objects.returns_value_objct import ReturnsValueObject


class SellOperationCapitalGainEntity(OperationCapitalGainEntity):
    returns: ReturnsValueObject
    total_value: Decimal

    @root_validator(pre=True)
    def default_new_operation_weighted_average_pricee(
        cls,
        values,
    ) -> Decimal:
        values["new_operation_weighted_average_price"] = values[
            "operation_weighted_average_price"
        ]

        return values

    @root_validator(pre=True)
    def default_new_operations_total_quantity(
        cls,
        values,
    ) -> int:
        values["new_operations_total_quantity"] = (
            values["operations_total_quantity"] - values["quantity"]
        )

        return values

    @validator("type")
    def check_type(cls, type):
        if type != OperationTypeEnum.SELL.value:
            raise ValueError("A Sell Operation cannot have a type different than sell")
        return type
