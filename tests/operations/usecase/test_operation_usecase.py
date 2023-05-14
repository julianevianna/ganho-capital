from unittest import TestCase

from system.application.dto.operation_list_input import OperationsListInput
from system.application.dto.taxes_list_output import TaxesListOutput
from system.application.usecases.operations.taxes_from_operations_list_usecase import (
    TaxesFromOperationsListUsecase,
)


def test_taxes_from_operations_list_usecase_sucess(
    mock_operations_list_input: OperationsListInput,
    mock_taxes_list_output: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(mock_operations_list_input)

    test_case.assertEqual(expected_result, result)
