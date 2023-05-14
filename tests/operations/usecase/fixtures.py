from ast import List
from decimal import Decimal

import pytest

from system.application.dto.operation_list_input import (
    OperationInput,
    OperationsListInput,
)
from system.application.dto.taxes_list_output import TaxesListOutput


@pytest.fixture
def mock_operations_list_input_usecase() -> OperationsListInput:
    operations_list_from_cli: List[OperationInput] = []

    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 5000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("20.00"), "quantity": 10000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("10.00"), "quantity": 5000}
        ),
    )

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_usecase():
    taxes_list: TaxesListOutput = []

    taxes_list.append(
        {
            "tax": Decimal("0.00"),
        },
    )
    taxes_list.append(
        {
            "tax": Decimal("10000.00"),
        },
    )
    taxes_list.append(
        {
            "tax": Decimal("0.00"),
        },
    )
    taxes_list.append(
        {
            "tax": Decimal("0.00"),
        },
    )

    return taxes_list
