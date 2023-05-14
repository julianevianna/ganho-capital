from decimal import Decimal
from typing import List

import pytest

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
def mock_buy_operation() -> BuyOperationCapitalGainEntity:
    return BuyOperationCapitalGainEntity(
        type="buy",
        unit_cost=Decimal("10.00"),
        quantity=10000,
        operations_total_quantity=5000,
        operation_weighted_average_price=Decimal("25.00"),
    )


@pytest.fixture
def mock_buy_operation_first_operation() -> BuyOperationCapitalGainEntity:
    return BuyOperationCapitalGainEntity(
        type="buy",
        unit_cost=Decimal("10.00"),
        quantity=10000,
        operations_total_quantity=0,
    )


@pytest.fixture
def mock_buy_operation_tax_different_zero() -> BuyOperationCapitalGainEntity:
    return BuyOperationCapitalGainEntity(
        type="buy",
        unit_cost=Decimal("10.00"),
        quantity=10000,
        operations_total_quantity=10000,
        tax=TaxValueObject(value=10, tax_rate=20),
    )


@pytest.fixture
def mock_sell_profit_operation() -> SellOperationCapitalGainEntity:
    return SellOperationCapitalGainEntity(
        type="sell",
        unit_cost=Decimal("20.00"),
        quantity=5000,
        operations_total_quantity=10000,
        operation_weighted_average_price=Decimal("10.00"),
    )


@pytest.fixture
def mock_sell_profit_with_previous_loss_resulting_loss_operation() -> (
    SellOperationCapitalGainEntity
):
    return SellOperationCapitalGainEntity(
        type="sell",
        unit_cost=Decimal("20.00"),
        quantity=5000,
        operations_total_quantity=10000,
        operation_weighted_average_price=Decimal("10.00"),
        previous_loss=Decimal("100000.00"),
    )


@pytest.fixture
def mock_sell_profit_with_previous_loss_resulting_zero_operation() -> (
    SellOperationCapitalGainEntity
):
    return SellOperationCapitalGainEntity(
        type="sell",
        unit_cost=Decimal("20.00"),
        quantity=5000,
        operations_total_quantity=10000,
        operation_weighted_average_price=Decimal("10.00"),
        previous_loss=Decimal("50000.00"),
    )


@pytest.fixture
def mock_sell_profit_with_previous_loss_resulting_non_minimum_profit_operation() -> (
    SellOperationCapitalGainEntity
):
    return SellOperationCapitalGainEntity(
        type="sell",
        unit_cost=Decimal("20.00"),
        quantity=5000,
        operations_total_quantity=10000,
        operation_weighted_average_price=Decimal("10.00"),
        previous_loss=Decimal("40000.00"),
    )


@pytest.fixture
def mock_sell_loss_operation() -> SellOperationCapitalGainEntity:
    return SellOperationCapitalGainEntity(
        type="sell",
        unit_cost=Decimal("5.00"),
        quantity=5000,
        operations_total_quantity=5000,
        operation_weighted_average_price=Decimal("10.00"),
    )


@pytest.fixture
def mock_sell_zero_operation() -> SellOperationCapitalGainEntity:
    return SellOperationCapitalGainEntity(
        type="sell",
        unit_cost=Decimal("10.00"),
        quantity=5000,
        operations_total_quantity=5000,
        operation_weighted_average_price=Decimal("10.00"),
    )


@pytest.fixture
def mock_sell_not_minunum_operation() -> SellOperationCapitalGainEntity:
    return SellOperationCapitalGainEntity(
        type="sell",
        unit_cost=Decimal("15.00"),
        quantity=50,
        operations_total_quantity=100,
        operation_weighted_average_price=Decimal("10.00"),
    )


@pytest.fixture
def mock_operations_list_entity() -> OperationListEntity:
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
