from decimal import Decimal

from system.domain.value_objects.base_value_object import BaseValueObject


class TaxValueObject(BaseValueObject):
    value: Decimal
    tax_rate: Decimal

    @property
    def tax_value(self):
        return self.value * self.tax_rate
