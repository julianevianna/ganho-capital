from decimal import Decimal
from unittest import TestCase

from pydantic import ValidationError

from system.application.enums.operation_type_enum import OperationTypeEnum
from system.domain.entities.sell_operation_capital_gain_entity import (
    SellOperationCapitalGainEntity,
)


def test_return_sell_operation_total_value(
    mock_sell_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_operation.total_value,
        Decimal("100000.00"),
    )


def test_return_sell_operation_new_operation_weighted_average_price(
    mock_sell_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_operation.new_operation_weighted_average_price,
        Decimal("10.00"),
    )


def test_return_sell_operation_new_operations_total_quantity(
    mock_sell_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_operation.new_operations_total_quantity,
        5000,
    )


def test_return_sell_operation_profit_sucess(
    mock_sell_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_operation.returns.returns,
        Decimal("50000.00"),
    )


def test_tax_sell_operation_profit_sucess(
    mock_sell_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_sell_profit_operation.tax.tax_value, Decimal("10000.00"))


def test_return_sell_operation_loss_sucess(
    mock_sell_loss_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_loss_operation.returns.returns,
        Decimal("-25000.00"),
    )


def test_tax_sell_operation_loss_sucess(
    mock_sell_loss_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_sell_loss_operation.tax.tax_value, Decimal("0.00"))


def test_return_sell_operation_zero_sucess(
    mock_sell_zero_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_sell_zero_operation.returns.returns, Decimal("0.00"))


def test_tax_sell_operation_zero_sucess(
    mock_sell_zero_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_sell_zero_operation.tax.tax_value, Decimal("0.00"))


def test_return_sell_operation_not_minunum_sucess(
    mock_sell_not_minunum_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_not_minunum_operation.returns.returns,
        Decimal("250.00"),
    )


def test_tax_sell_operation_not_minunum_sucess(
    mock_sell_not_minunum_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_not_minunum_operation.tax.tax_value,
        Decimal("0.00"),
    )


def test_type_sell_operation_sucess() -> None:
    test_case = TestCase()

    sell_operation_entity = SellOperationCapitalGainEntity(
        unit_cost=Decimal("10.00"),
        quantity=10000,
        operations_total_quantity=10000,
    )

    test_case.assertEqual(sell_operation_entity.type, OperationTypeEnum.SELL.value)


def test_type_sell_operation_fail() -> None:
    test_case = TestCase()

    with test_case.assertRaises(ValidationError) as error:
        SellOperationCapitalGainEntity(
            type=OperationTypeEnum.BUY.value,
            unit_cost=Decimal("10.00"),
            quantity=10000,
            operations_total_quantity=10000,
        )

    test_case.assertIn(
        "A Sell Operation cannot have a type different than sell",
        str(error.exception),
    )
