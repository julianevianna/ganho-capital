from decimal import Decimal

from pydantic import root_validator, validator

from system.application.enums.operation_type_enum import OperationTypeEnum
from system.domain.entities.operation_capital_gain_entity import (
    OperationCapitalGainEntity,
)
from system.domain.value_objects.returns_value_objct import ReturnsValueObject
from system.domain.value_objects.tax_value_object import TaxValueObject


class SellOperationCapitalGainEntity(OperationCapitalGainEntity):
    returns: ReturnsValueObject
    total_value: Decimal

    @root_validator(pre=True)
    def default_total_value(
        cls,
        values,
    ) -> Decimal:
        values["total_value"] = values["unit_cost"] * values["quantity"]

        return values

    @root_validator(pre=True)
    def default_new_operation_weighted_average_price(
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

    @root_validator(pre=True)
    def default_returns(cls, values) -> ReturnsValueObject:
        values["returns"] = ReturnsValueObject(
            average_price=values["operation_weighted_average_price"],
            quantity=values["quantity"],
            total_value=values["total_value"],
            loss=values["loss"] if "loss" in values else None,
        )  # type: ignore

        return values

    @root_validator(pre=True)
    def default_tax(cls, values) -> TaxValueObject:
        if values["returns"].returns > Decimal("20000.00"):
            returns_value = values["returns"].returns
        else:
            returns_value = Decimal("0.00")

        values["tax"] = TaxValueObject(
            value=returns_value,
            tax_rate=Decimal("20.00"),
        )

        return values

    @validator("type")
    def check_type(cls, type):
        if type != OperationTypeEnum.SELL.value:
            raise ValueError("A Sell Operation cannot have a type different than sell")
        return type
