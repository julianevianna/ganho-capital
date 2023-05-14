from typing import Dict, List
from unittest import TestCase

from pydantic import ValidationError

from system.application.dto.operation_list_input import (
    OperationInput,
    OperationsListInput,
)


def test_input_fields_sucess(
    mock_operations_list_cli_sucess: List[Dict],
    mock_operations_list_input_sucess: OperationsListInput,
):
    test_case = TestCase()

    operation_list_input = OperationsListInput(
        operation_list=[
            OperationInput.parse_obj(operation)
            for operation in mock_operations_list_cli_sucess
        ],
    )

    test_case.assertEqual(operation_list_input, mock_operations_list_input_sucess)


def test_input_operation_field_fail(
    mock_operations_list_cli_operation_field_fail: List[Dict],
):
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        OperationsListInput(
            operation_list=[
                OperationInput.parse_obj(operation)
                for operation in mock_operations_list_cli_operation_field_fail
            ],
        )


def test_input_unit_cost_field_fail(
    mock_operations_list_cli_unit_cost_field_fail: List[Dict],
):
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        OperationsListInput(
            operation_list=[
                OperationInput.parse_obj(operation)
                for operation in mock_operations_list_cli_unit_cost_field_fail
            ],
        )


def test_input_unit_quantity_fail(
    mock_operations_list_cli_quantity_field_fail: List[Dict],
):
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        OperationsListInput(
            operation_list=[
                OperationInput.parse_obj(operation)
                for operation in mock_operations_list_cli_quantity_field_fail
            ],
        )


def test_input_missing_field_fail(
    mock_operations_list_cli_missing_field_fail: List[Dict],
):
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        OperationsListInput(
            operation_list=[
                OperationInput.parse_obj(operation)
                for operation in mock_operations_list_cli_missing_field_fail
            ],
        )


def test_input_wrong_field_fail(
    mock_operations_list_cli_wrong_field_fail: List[Dict],
):
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        OperationsListInput(
            operation_list=[
                OperationInput.parse_obj(operation)
                for operation in mock_operations_list_cli_wrong_field_fail
            ],
        )


def test_input_wrong_operation_type_fail(
    mock_operations_list_cli_wrong_operation_type_fail: List[Dict],
):
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        OperationsListInput(
            operation_list=[
                OperationInput.parse_obj(operation)
                for operation in mock_operations_list_cli_wrong_operation_type_fail
            ],
        )


def test_input_operation_type_case_insensitive_sucess(
    mock_operations_list_cli_operation_type_case_insensitive_sucess: List[Dict],
    mock_operations_list_input_sucess: OperationsListInput,
):
    test_case = TestCase()

    operation_list_input = OperationsListInput(
        operation_list=[
            OperationInput.parse_obj(operation)
            for operation in mock_operations_list_cli_operation_type_case_insensitive_sucess
        ],
    )

    test_case.assertEqual(operation_list_input, mock_operations_list_input_sucess)


def test_input_wrong_unit_cost_format_fail(
    mock_operations_list_cli_wrong_unit_cost_format_fail: List[Dict],
):
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        OperationsListInput(
            operation_list=[
                OperationInput.parse_obj(operation)
                for operation in mock_operations_list_cli_wrong_unit_cost_format_fail
            ],
        )


def test_input_wrong_quantity_format_fail(
    mock_operations_list_cli_wrong_quantity_format_fail: List[Dict],
):
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        OperationsListInput(
            operation_list=[
                OperationInput.parse_obj(operation)
                for operation in mock_operations_list_cli_wrong_quantity_format_fail
            ],
        )
