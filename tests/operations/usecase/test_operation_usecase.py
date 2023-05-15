from unittest import TestCase

from system.application.dto.operation_list_input import OperationsListInput
from system.application.dto.taxes_list_output import TaxesListOutput
from system.application.usecases.operations.taxes_from_operations_list_usecase import (
    TaxesFromOperationsListUsecase,
)


def test_taxes_from_operations_list_case_1_sucess(
    mock_operations_list_input_case_1_sucess: OperationsListInput,
    mock_taxes_list_output_case_1_sucess: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output_case_1_sucess

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(
        mock_operations_list_input_case_1_sucess,
    )

    test_case.assertEqual(expected_result, result)


def test_taxes_from_operations_list_case_2_sucess(
    mock_operations_list_input_case_2_sucess: OperationsListInput,
    mock_taxes_list_output_case_2_sucess: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output_case_2_sucess

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(
        mock_operations_list_input_case_2_sucess,
    )

    test_case.assertEqual(expected_result, result)


def test_taxes_from_operations_list_case_3_sucess(
    mock_operations_list_input_case_3_sucess: OperationsListInput,
    mock_taxes_list_output_case_3_sucess: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output_case_3_sucess

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(
        mock_operations_list_input_case_3_sucess,
    )

    test_case.assertEqual(expected_result, result)


def test_taxes_from_operations_list_case_4_sucess(
    mock_operations_list_input_case_4_sucess: OperationsListInput,
    mock_taxes_list_output_case_4_sucess: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output_case_4_sucess

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(
        mock_operations_list_input_case_4_sucess,
    )

    test_case.assertEqual(expected_result, result)


def test_taxes_from_operations_list_case_5_sucess(
    mock_operations_list_input_case_5_sucess: OperationsListInput,
    mock_taxes_list_output_case_5_sucess: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output_case_5_sucess

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(
        mock_operations_list_input_case_5_sucess,
    )

    test_case.assertEqual(expected_result, result)


def test_taxes_from_operations_list_case_6_sucess(
    mock_operations_list_input_case_6_sucess: OperationsListInput,
    mock_taxes_list_output_case_6_sucess: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output_case_6_sucess

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(
        mock_operations_list_input_case_6_sucess,
    )

    test_case.assertEqual(expected_result, result)


def test_taxes_from_operations_list_case_7_sucess(
    mock_operations_list_input_case_7_sucess: OperationsListInput,
    mock_taxes_list_output_case_7_sucess: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output_case_7_sucess

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(
        mock_operations_list_input_case_7_sucess,
    )

    test_case.assertEqual(expected_result, result)


def test_taxes_from_operations_list_case_8_sucess(
    mock_operations_list_input_case_8_sucess: OperationsListInput,
    mock_taxes_list_output_case_8_sucess: TaxesListOutput,
) -> None:
    test_case = TestCase()

    expected_result: TaxesListOutput = mock_taxes_list_output_case_8_sucess

    taxes_from_operations_list_usecase = TaxesFromOperationsListUsecase()

    result = taxes_from_operations_list_usecase.execute(
        mock_operations_list_input_case_8_sucess,
    )

    test_case.assertEqual(expected_result, result)
