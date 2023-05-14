from decimal import Decimal

from system.application.dto.operation_list_input import OperationsListInput
from system.application.dto.taxes_list_output import TaxesListOutput
from system.application.usecases.usecase import UseCase


class TaxesFromOperationsListUsecase(UseCase):
    def execute(
        self,
        input_usecase: OperationsListInput,
    ) -> TaxesListOutput:
        return TaxesListOutput(taxes=[Decimal("10.00")])
