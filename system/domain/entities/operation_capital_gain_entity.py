from decimal import Decimal

from pydantic import root_validator

from system.domain.entities.operation_entity import OperationEntity
from system.domain.value_objects.tax_value_object import TaxValueObject


class OperationCapitalGainEntity(OperationEntity):
    operations_total_quantity: int
    operation_weighted_average_price: Decimal

    new_operations_total_quantity: int
    new_operation_weighted_average_price: Decimal

    tax: TaxValueObject

    @root_validator(pre=True)
    def default_operations_total_quantity(
        cls,
        values,
    ) -> Decimal:
        if (
            "operations_total_quantity" not in values
            or values["operations_total_quantity"] is None
        ):
            values["operations_total_quantity"] = 0
        return values

    @root_validator(pre=True)
    def default_operation_weighted_average_price(
        cls,
        values,
    ) -> Decimal:
        if (
            "operation_weighted_average_price" not in values
            or values["operation_weighted_average_price"] is None
        ):
            values["operation_weighted_average_price"] = Decimal("0.00")
        return values
