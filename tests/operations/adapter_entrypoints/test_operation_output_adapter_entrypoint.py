from unittest import TestCase

from pydantic import ValidationError

from system.application.dto.taxes_list_output import TaxesListOutput
from system.domain.entities.operation_list_entity import OperationListEntity


def test_output_operation_taxes_list_sucess(
    mock_operations_list_entity_to_get_taxes: OperationListEntity,
    mock_taxes_list_output_sucess: TaxesListOutput,
):
    test_case = TestCase()

    taxes_list_output = TaxesListOutput(
        taxes=list(
            map(
                lambda operation: operation.tax.tax_value,
                mock_operations_list_entity_to_get_taxes.operations,
            ),
        ),
    )

    test_case.assertEqual(taxes_list_output, mock_taxes_list_output_sucess)


def test_output_operation_taxes_list_fail():
    test_case = TestCase()

    with test_case.assertRaises(ValidationError):
        TaxesListOutput(
            taxes=[
                "tax1",
                "tax2",
            ],
        )
