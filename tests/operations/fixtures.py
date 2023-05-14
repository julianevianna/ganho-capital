from decimal import Decimal

import pytest

from system.application.dto.operation_list_input import (
    OperationInput,
    OperationsListInput,
)
from system.application.dto.taxes_list_output import TaxesListOutput
from system.domain.entities.buy_operation_capital_gain_entity import (
    BuyOperationCapitalGainEntity,
)


@pytest.fixture
def mock_buy_operation() -> BuyOperationCapitalGainEntity:
    return BuyOperationCapitalGainEntity(
        type="buy",
        unit_cost=Decimal("10.00"),
        quantity=10000,
        operations_total_quantity=10000,
    )


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
def mock_operations_list_input() -> OperationsListInput:
    operations_list: OperationsListInput = []

    operations_list.append(
        OperationInput(
            **{"operation": "buy", "unit_cost": Decimal("10.00"), "quantity": 10000}
        ),
    )
    operations_list.append(
        OperationInput(
            **{"operation": "sell", "unit_cost": Decimal("20.00"), "quantity": 5000}
        ),
    )
    operations_list.append(
        OperationInput(
            **{"operation": "buy", "unit_cost": Decimal("20.00"), "quantity": 10000}
        ),
    )
    operations_list.append(
        OperationInput(
            **{"operation": "sell", "unit_cost": Decimal("10.00"), "quantity": 5000}
        ),
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
