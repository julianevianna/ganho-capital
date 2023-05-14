from decimal import Decimal
from typing import List

from system.application.dto.output import Output


class TaxesListOutput(Output):
    taxes: List[Decimal]
