from system.domain.entities.operation_entity import OperationEntity
from system.domain.value_objects.tax_value_object import TaxValueObject


class OperationCapitalGainEntity(OperationEntity):
    operations_total_quantity: int = 0
    tax: TaxValueObject
