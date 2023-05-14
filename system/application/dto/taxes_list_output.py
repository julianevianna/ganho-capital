from decimal import ROUND_HALF_UP, Decimal
from typing import List

from pydantic import validator

from system.application.dto.output import Output


class TaxesListOutput(Output):
    taxes: List[Decimal]

    @validator("taxes", pre=True)
    def check_taxes(cls, value):
        for index, tax in enumerate(value):
            value[index] = Decimal(tax).quantize(
                Decimal("0.00"),
                rounding=ROUND_HALF_UP,
            )

        return value
