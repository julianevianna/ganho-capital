from decimal import Decimal

from pydantic import root_validator

from system.application.enums.operation_type_enum import OperationTypeEnum
from system.domain.entities.operation_capital_gain_entity import (
    OperationCapitalGainEntity,
)
from system.domain.value_objects.tax_value_object import TaxValueObject


class BuyOperationCapitalGainEntity(OperationCapitalGainEntity):
    @root_validator(pre=True)
    def calculate_new_weighted_average_price(
        cls,
        values,
    ) -> Decimal:
        values["new_operation_weighted_average_price"] = (
            (
                values["operations_total_quantity"]
                * values["operation_weighted_average_price"]
            )
            + (values["quantity"] * values["unit_cost"])
        ) / (values["operations_total_quantity"] + values["quantity"])

        return values

    @root_validator(pre=True)
    def calculate_new_operations_total_quantity(
        cls,
        values,
    ) -> int:
        values["new_operations_total_quantity"] = (
            values["operations_total_quantity"] + values["quantity"]
        )

        return values

    @root_validator(pre=True)
    def default_tax(cls, values):
        if "tax" not in values or values["tax"] is None:
            values["tax"] = TaxValueObject(value=0, tax_rate=20)
        if values["tax"].value != 0:
            raise ValueError("A Buy Operation doesent have tax")
        return values

    @root_validator(pre=True)
    def default_type(cls, values):
        if "type" not in values or values["type"] is None:
            values["type"] = OperationTypeEnum.BUY.value
        elif values["type"] != OperationTypeEnum.BUY.value:
            raise ValueError("A Buy Operation cannot have a type different than buy")
        return values
