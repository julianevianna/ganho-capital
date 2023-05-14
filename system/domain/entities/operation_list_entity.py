from decimal import Decimal
from typing import List

from pydantic import root_validator

from system.domain.entities.base_entity import BaseEntity
from system.domain.entities.operation_capital_gain_entity import (
    OperationCapitalGainEntity,
)


class OperationListEntity(BaseEntity):
    operations: List[OperationCapitalGainEntity]
    tax_rate: Decimal
    weighted_average_price_list: List[Decimal]

    @root_validator(pre=True)
    def calculate_weighted_average_price_list(cls, values):
        values["weighted_average_price_list"] = []
        new_operations_total_quantity = 0

        for index, operation in enumerate(values["operations"]):
            operation.operations_total_quantity = new_operations_total_quantity
            operation_quantity = operation.quantity
            operation_unity_cost = operation.unit_cost
            operation_type = operation.type

            weighted_average_price = (
                values["weighted_average_price_list"][index - 1] if index != 0 else 0
            )

            new_weighted_average_price = cls.calculate_new_weighted_average_price(
                new_operations_total_quantity,
                weighted_average_price,
                operation_quantity,
                operation_unity_cost,
                operation_type,
            )

            values["weighted_average_price_list"].append(new_weighted_average_price)

            new_operations_total_quantity = cls.calculate_new_operations_total_quantity(
                new_operations_total_quantity,
                operation_quantity,
                operation_type,
            )

        return values

    @staticmethod
    def calculate_new_weighted_average_price(
        operations_total_quantity: int,
        weighted_average_price: Decimal,
        operation_quantity: int,
        operation_unity_cost: Decimal,
        operation_type: str,
    ) -> Decimal:
        new_weighted_average_price = {
            "buy": (
                (operations_total_quantity * weighted_average_price)
                + (operation_quantity * operation_unity_cost)
            )
            / (operations_total_quantity + operation_quantity),
            "sell": weighted_average_price,
        }

        return new_weighted_average_price.get(operation_type) or Decimal("0.00")

    @staticmethod
    def calculate_new_operations_total_quantity(
        operations_total_quantity: int,
        operation_quantity: int,
        operation_type: str,
    ) -> int:
        new_operations_total_quantity = {
            "buy": operations_total_quantity + operation_quantity,
            "sell": operations_total_quantity - operation_quantity,
        }

        return new_operations_total_quantity.get(operation_type) or 0
