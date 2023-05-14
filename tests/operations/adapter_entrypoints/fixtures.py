from decimal import Decimal
from typing import Dict, List

import pytest

from system.application.dto.operation_list_input import (
    OperationInput,
    OperationsListInput,
)
from system.application.dto.taxes_list_output import TaxesListOutput
from system.domain.entities.buy_operation_capital_gain_entity import (
    BuyOperationCapitalGainEntity,
)
from system.domain.entities.operation_capital_gain_entity import (
    OperationCapitalGainEntity,
)
from system.domain.entities.operation_list_entity import OperationListEntity
from system.domain.entities.sell_operation_capital_gain_entity import (
    SellOperationCapitalGainEntity,
)
from system.domain.value_objects.returns_value_objct import ReturnsValueObject
from system.domain.value_objects.tax_value_object import TaxValueObject


@pytest.fixture
def mock_operations_list_cli_sucess() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 10.00, "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_operation_field_fail() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"operations": "buy", "unit-cost": 10.00, "quantity": 10000},
    )
    operations_list.append(
        {"operations": "sell", "unit-cost": 20.00, "quantity": 5000},
    )
    operations_list.append(
        {"operations": "buy", "unit-cost": 20.00, "quantity": 10000},
    )
    operations_list.append(
        {"operations": "sell", "unit-cost": 10.00, "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_unit_cost_field_fail() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"operation": "buy", "units-cost": 10.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "units-cost": 20.00, "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "units-cost": 20.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "units-cost": 10.00, "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_quantity_field_fail() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"operation": "buy", "unit-cost": 10.00, "quantiti": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 10.00, "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_missing_field_fail() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"unit-cost": 10.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": 20.00},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 10.00, "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_wrong_field_fail() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {
            "operation": "buy",
            "unit-cost": 10.00,
            "quantity": 10000,
            "total-value": 100000.00,
        },
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 10.00, "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_wrong_operation_type_fail() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"operation": "loss", "unit-cost": 10.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "loss", "unit-cost": 20.00, "quantity": 5000},
    )
    operations_list.append(
        {"operation": "loss", "unit-cost": 20.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "loss", "unit-cost": 10.00, "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_operation_type_case_insensitive_sucess() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"operation": "BUY", "unit-cost": 10.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "Sell", "unit-cost": 20.00, "quantity": 5000},
    )
    operations_list.append(
        {"operation": "BuY", "unit-cost": 20.00, "quantity": 10000},
    )
    operations_list.append(
        {"operation": "seLL", "unit-cost": 10.00, "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_wrong_unit_cost_format_fail() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"operation": "buy", "unit-cost": "ten", "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": "ten", "quantity": 5000},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": "ten", "quantity": 10000},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": "ten", "quantity": 5000},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_cli_wrong_quantity_format_fail() -> List[Dict]:
    operations_list = []

    operations_list.append(
        {"operation": "buy", "unit-cost": 10.00, "quantity": "ten"},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 20.00, "quantity": "ten"},
    )
    operations_list.append(
        {"operation": "buy", "unit-cost": 20.00, "quantity": "ten"},
    )
    operations_list.append(
        {"operation": "sell", "unit-cost": 10.00, "quantity": "ten"},
    )

    return operations_list


@pytest.fixture
def mock_operations_list_input_sucess() -> OperationsListInput:
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
def mock_taxes_list_output_sucess() -> TaxesListOutput:
    taxes_list: List[Decimal] = []

    taxes_list.append(Decimal("0.00"))
    taxes_list.append(Decimal("0.00"))
    taxes_list.append(Decimal("0.00"))

    return TaxesListOutput(taxes=taxes_list)


@pytest.fixture
def mock_operations_list_entity_to_get_taxes() -> OperationListEntity:
    operations_list: List[OperationCapitalGainEntity] = []

    operations_list.append(
        BuyOperationCapitalGainEntity(
            type="buy",
            unit_cost=Decimal("10.00"),
            quantity=10000,
        ),
    )
    operations_list.append(
        BuyOperationCapitalGainEntity(
            type="buy",
            unit_cost=Decimal("25.00"),
            quantity=5000,
            operation_weighted_average_price=operations_list[
                -1
            ].new_operation_weighted_average_price,
            operations_total_quantity=operations_list[-1].new_operations_total_quantity,
        ),
    )
    operations_list.append(
        SellOperationCapitalGainEntity(
            type="sell",
            unit_cost=Decimal("15.00"),
            quantity=10000,
            tax=TaxValueObject(
                value=0,
                tax_rate=20,
            ),
            returns=ReturnsValueObject(
                average_price=Decimal("15.00"),
                quantity=10000,
                total_value=Decimal("150000.00"),
            ),
            total_value=Decimal("150000.00"),
            operation_weighted_average_price=operations_list[
                -1
            ].new_operation_weighted_average_price,
            operations_total_quantity=operations_list[-1].new_operations_total_quantity,
        ),
    )

    operations_list_entity = OperationListEntity(
        operations=operations_list,
        tax_rate=Decimal("20.00"),
    )

    return operations_list_entity
