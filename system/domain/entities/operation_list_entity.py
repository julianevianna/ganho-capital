from decimal import Decimal
from typing import List

from pydantic import root_validator

from system.application.enums.operation_type_enum import OperationTypeEnum
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

        for index, operation in enumerate(values["operations"]):
            if operation.type == OperationTypeEnum.BUY.value:
                operations_total_quantity = operation.operations_total_quantity
                weighted_average_price = (
                    values["weighted_average_price_list"][index - 1]
                    if index != 0
                    else 0
                )

                operation_quantity = operation.quantity
                operation_unity_cost = operation.unit_cost

                new_weighted_average_price = cls.calculate_new_weighted_average_price(
                    operations_total_quantity,
                    weighted_average_price,
                    operation_quantity,
                    operation_unity_cost,
                )

            else:
                new_weighted_average_price = values["weighted_average_price_list"][
                    index - 1
                ]

            values["weighted_average_price_list"].append(new_weighted_average_price)

        return values

    @staticmethod
    def calculate_new_weighted_average_price(
        operations_total_quantity: int,
        weighted_average_price: Decimal,
        operation_quantity: int,
        operation_unity_cost: Decimal,
    ) -> Decimal:
        return (
            (operations_total_quantity * weighted_average_price)
            + (operation_quantity * operation_unity_cost)
        ) / (operations_total_quantity + operation_quantity)

    @staticmethod
    def calculate_operations_total_quantity(
        operations_total_quantity: int,
        operation_quantity: int,
        operation_type: OperationTypeEnum,
    ) -> int:
        new_operations_total_quantity = {
            "buy": operations_total_quantity + operation_quantity,
            "sell": operations_total_quantity - operation_quantity,
        }

        return new_operations_total_quantity.get(operation_type.value) or 0
