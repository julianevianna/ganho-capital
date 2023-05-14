from decimal import Decimal
from unittest import TestCase

from pydantic import ValidationError

from system.application.enums.operation_type_enum import OperationTypeEnum
from system.domain.entities.sell_operation_capital_gain_entity import (
    SellOperationCapitalGainEntity,
)
from system.domain.value_objects.returns_value_objct import ReturnsValueObject
from system.domain.value_objects.tax_value_object import TaxValueObject


def test_sell_operation_total_value(
    mock_sell_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_operation.total_value,
        Decimal("100000.00"),
    )


def test_sell_operation_new_operation_weighted_average_price(
    mock_sell_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_operation.new_operation_weighted_average_price,
        Decimal("10.00"),
    )


def test_sell_operation_new_operations_total_quantity(
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


def test_return_sell_operation_profit_with_previous_loss_resulting_loss_sucess(
    mock_sell_profit_with_previous_loss_resulting_loss_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_with_previous_loss_resulting_loss_operation.returns.returns,
        Decimal("-50000.00"),
    )


def test_tax_sell_operation_profit_with_previous_loss_resulting_loss_sucess(
    mock_sell_profit_with_previous_loss_resulting_loss_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_with_previous_loss_resulting_loss_operation.tax.tax_value,
        Decimal("0.00"),
    )


def test_return_sell_operation_profit_with_previous_loss_resulting_zero_sucess(
    mock_sell_profit_with_previous_loss_resulting_zero_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_with_previous_loss_resulting_zero_operation.returns.returns,
        Decimal("0.00"),
    )


def test_tax_sell_operation_profit_with_previous_loss_resulting_zero_sucess(
    mock_sell_profit_with_previous_loss_resulting_zero_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_with_previous_loss_resulting_zero_operation.tax.tax_value,
        Decimal("0.00"),
    )


def test_return_sell_operation_profit_with_previous_loss_resulting_non_minimum_profit_sucess(
    mock_sell_profit_with_previous_loss_resulting_non_minimum_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_with_previous_loss_resulting_non_minimum_profit_operation.returns.returns,
        Decimal("10000.00"),
    )


def test_tax_sell_operation_profit_with_previous_loss_resulting_non_minimum_profit_sucess(
    mock_sell_profit_with_previous_loss_resulting_non_minimum_profit_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_sell_profit_with_previous_loss_resulting_non_minimum_profit_operation.tax.tax_value,
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


def test_tax_entity_decimals_round_sucess(
    mock_tax_entity_decimals_round_sucess: TaxValueObject,
) -> None:
    test_case = TestCase()

    tax_value_object = TaxValueObject(
        value=Decimal("20.378"),
        tax_rate=Decimal("4.665"),
    )

    test_case.assertEqual(tax_value_object, mock_tax_entity_decimals_round_sucess)


def test_returns_entity_decimals_round_success(
    mock_returns_entity_decimals_round_success: ReturnsValueObject,
) -> None:
    test_case = TestCase()

    tax_value_object = ReturnsValueObject(
        average_price=Decimal("20.378"),
        quantity=10,
        total_value=Decimal("203.80"),
        previous_loss=Decimal("10.326"),
    )

    test_case.assertEqual(tax_value_object, mock_returns_entity_decimals_round_success)


def test_sell_operation_gain_entity_decimals_round_success(
    mock_sell_operation_gain_entity_decimals_round_success: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    sell_operation_gain_entity = SellOperationCapitalGainEntity(
        unit_cost=Decimal("10.0026"),
        quantity=10,
        operations_total_quantity=100,
        operation_weighted_average_price=Decimal("5.326"),
        previous_loss=Decimal("7.356"),
    )

    test_case.assertEqual(
        sell_operation_gain_entity,
        mock_sell_operation_gain_entity_decimals_round_success,
    )
