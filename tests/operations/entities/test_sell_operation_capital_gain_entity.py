from decimal import Decimal
from unittest import TestCase

from system.domain.entities.sell_operation_capital_gain_entity import (
    SellOperationCapitalGainEntity,
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
