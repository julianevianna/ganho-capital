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


@pytest.fixture
def mock_operations_list_input_case_2_sucess() -> OperationsListInput:
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
            **{"operation": "sell", "unit-cost": Decimal("5.00"), "quantity": 5000}
        ),
    )

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_case_2_sucess():
    return TaxesListOutput(
        taxes=[Decimal("0.00"), Decimal("10000.00"), Decimal("0.00")],
    )


@pytest.fixture
def mock_operations_list_input_case_3_sucess() -> OperationsListInput:
    operations_list_from_cli: List[OperationInput] = []

    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("5.00"), "quantity": 5000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 3000}
        ),
    )

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_case_3_sucess():
    return TaxesListOutput(taxes=[Decimal("0.00"), Decimal("0.00"), Decimal("1000.00")])


@pytest.fixture
def mock_operations_list_input_case_4_sucess() -> OperationsListInput:
    operations_list_from_cli: List[OperationInput] = []

    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("25.00"), "quantity": 5000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("15.00"), "quantity": 10000}
        ),
    )

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_case_4_sucess():
    return TaxesListOutput(taxes=[Decimal("0.00"), Decimal("0.00"), Decimal("0.00")])


@pytest.fixture
def mock_operations_list_input_case_5_sucess() -> OperationsListInput:
    operations_list_from_cli: List[OperationInput] = []

    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("25.00"), "quantity": 5000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("15.00"), "quantity": 10000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("25.00"), "quantity": 5000}
        ),
    )

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_case_5_sucess():
    return TaxesListOutput(
        taxes=[Decimal("0.00"), Decimal("0.00"), Decimal("0.00"), Decimal("10000.00")],
    )


@pytest.fixture
def mock_operations_list_input_case_6_sucess() -> OperationsListInput:
    operations_list_from_cli: List[OperationInput] = []

    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("2.00"), "quantity": 5000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 2000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 2000}
        ),
    )
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("25.00"), "quantity": 1000}
        ),
    )

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_case_6_sucess():
    return TaxesListOutput(
        taxes=[
            Decimal("0.00"),
            Decimal("0.00"),
            Decimal("0.00"),
            Decimal("0.00"),
            Decimal("3000.00"),
        ],
    )


@pytest.fixture
def mock_operations_list_input_case_7_sucess() -> OperationsListInput:
    operations_list_from_cli: List[OperationInput] = []

    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("10.00"), "quantity": 10000}
        ),
    ),
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("2.00"), "quantity": 5000}
        ),
    ),
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 2000}
        ),
    ),
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("20.00"), "quantity": 2000}
        ),
    ),
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("25.00"), "quantity": 1000}
        ),
    ),
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "buy", "unit-cost": Decimal("20.00"), "quantity": 10000}
        ),
    ),
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("15.00"), "quantity": 5000}
        ),
    ),
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("30.00"), "quantity": 4350}
        ),
    ),
    operations_list_from_cli.append(
        OperationInput(
            **{"operation": "sell", "unit-cost": Decimal("30.00"), "quantity": 650}
        ),
    ),

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_case_7_sucess():
    return TaxesListOutput(
        taxes=[
            Decimal("0.00"),
            Decimal("0.00"),
            Decimal("0.00"),
            Decimal("0.00"),
            Decimal("3000.00"),
            Decimal("0.00"),
            Decimal("0.00"),
            Decimal("3700.00"),
            Decimal("0.00"),
        ],
    )


@pytest.fixture
def mock_operations_list_input_case_8_sucess() -> OperationsListInput:
    operations_list_from_cli: List[OperationInput] = []

    operations_list_from_cli.append(
        OperationInput(**{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}),
    )
    operations_list_from_cli.append(
        OperationInput(**{"operation": "sell", "unit-cost": 50.00, "quantity": 10000}),
    )
    operations_list_from_cli.append(
        OperationInput(**{"operation": "buy", "unit-cost": 20.00, "quantity": 10000}),
    )
    operations_list_from_cli.append(
        OperationInput(**{"operation": "sell", "unit-cost": 50.00, "quantity": 10000}),
    )

    operations_list_input = OperationsListInput(operation_list=operations_list_from_cli)

    return operations_list_input


@pytest.fixture
def mock_taxes_list_output_case_8_sucess():
    return TaxesListOutput(
        taxes=[
            Decimal("0.00"),
            Decimal("80000.00"),
            Decimal("0.00"),
            Decimal("60000.00"),
        ],
    )
