from pydantic import root_validator, validator

from system.application.enums.operation_type_enum import OperationTypeEnum
from system.domain.entities.operation_capital_gain_entity import (
    OperationCapitalGainEntity,
)
from system.domain.value_objects.tax_value_object import TaxValueObject


class BuyOperationCapitalGainEntity(OperationCapitalGainEntity):
    @root_validator(pre=True)
    def default_tax(cls, values):
        if "tax" not in values or values["tax"] is None:
            values["tax"] = TaxValueObject(value=0, tax_rate=20)
        return values

    @validator("type")
    def check_type(cls, type):
        if type != OperationTypeEnum.BUY.value:
            raise ValueError("A Buy Operation cannot have a type different than buy")
        return type
