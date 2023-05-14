from decimal import Decimal
from typing import List

import pytest

from system.application.dto.operation_list_input import (
    OperationInput,
    OperationsListInput,
)
from system.application.dto.taxes_list_output import TaxesListOutput


@pytest.fixture
def mock_operations_list_cli() -> OperationsListInput:
    operations_list = []

    operations_list.append(
        {"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": Decimal("20.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("10.00"), "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_operation_field_fail() -> OperationsListInput:
    operations_list = []

    operations_list.append(
        {"operations": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operations": "sell", "unit-cost": Decimal("20.00"), "quantity": 5000},
    )
    operations_list.append(
        {"operations": "buy", "unit-cost": Decimal("20.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operations": "sell", "unit-cost": Decimal("10.00"), "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_unit_cost_field_fail() -> OperationsListInput:
    operations_list = []

    operations_list.append(
        {"operation": "buy", "units-cost": Decimal("10.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "units-cost": Decimal("20.00"), "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "units-cost": Decimal("20.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "units-cost": Decimal("10.00"), "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_quantity_field_fail() -> OperationsListInput:
    operations_list = []

    operations_list.append(
        {"operation": "buy", "unit-cost": Decimal("10.00"), "quantiti": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": Decimal("20.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("10.00"), "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_missing_field_fail() -> OperationsListInput:
    operations_list = []

    operations_list.append(
        {"unit-cost": Decimal("10.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": Decimal("20.00")},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("10.00"), "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_input() -> OperationsListInput:
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
def mock_operations_list_cli_wrong_field_fail() -> OperationsListInput:
    operations_list = []

    operations_list.append(
        {
            "operation": "buy",
            "unit-cost": Decimal("10.00"),
            "quantity": 10000,
            "total-value": Decimal("100000.00"),
        },
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": Decimal("20.00"), "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("10.00"), "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_taxes_list_output():
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
