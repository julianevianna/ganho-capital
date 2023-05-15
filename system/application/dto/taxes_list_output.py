import json
from decimal import ROUND_HALF_UP, Decimal
from typing import List

from pydantic import validator

from system.application.dto.output import Output


class TaxesListOutput(Output):
    taxes: List[Decimal]

    @validator("taxes", pre=True)
    def check_taxes(cls, value):
        for index, tax in enumerate(value):
            if isinstance(tax, float):
                tax = Decimal(str(tax))
            value[index] = (
                Decimal(tax).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
                if isinstance(tax, Decimal)
                else tax
            )

        return value

    def __str__(self):
        return json.dumps([{"tax": float("{:.2f}".format(x))} for x in self.taxes])
