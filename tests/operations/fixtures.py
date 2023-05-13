import pytest
from decimal import Decimal


@pytest.fixture
def operations_list_input():
    operations_list = []

    operations_list.append(
        {"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000}
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 5000}
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": Decimal("20.00"), "quantity": 10000}
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": Decimal("10.00"), "quantity": 5000}
    )

    return operations_list


@pytest.fixture
def taxes_list_output():
    taxes_list = []

    taxes_list.append(
        {
            "tax": Decimal("0.00"),
        }
    )
    taxes_list.append(
        {
            "tax": Decimal("10000.00"),
        }
    )
    taxes_list.append(
        {
            "tax": Decimal("0.00"),
        }
    )
    taxes_list.append(
        {
            "tax": Decimal("0.00"),
        }
    )

    return taxes_list
