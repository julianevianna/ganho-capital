from ast import List
from decimal import Decimal

import pytest

from system.application.dto.operation_list_input import (
    OperationInput,
    OperationsListInput,
)
from system.application.dto.taxes_list_output import TaxesListOutput


@pytest.fixture
def mock_operations_list_input_case_1_sucess() -> OperationsListInput:
    operations_list_from_cli: List[OperationInput] = []

    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 100}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("15.00"), "quantity": 50}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 50}
        ),
    )

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_case_1_sucess():
    return TaxesListOutput(taxes=[Decimal("0.00"), Decimal("0.00"), Decimal("0.00")])
