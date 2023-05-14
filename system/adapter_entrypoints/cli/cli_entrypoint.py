from system.application.dto.operation_list_input import OperationsListInput
from system.application.dto.taxes_list_output import TaxesListOutput
from system.application.usecases.operations.taxes_from_operations_list_usecase import \
    TaxesFromOperationsListUsecase


class CLIHandler:
    def operations_list_input(
        self,
        operation_list: OperationsListInput,
    ) -> TaxesListOutput:
        return TaxesFromOperationsListUsecase().execute(operation_list)
