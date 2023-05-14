from decimal import Decimal
from unittest import TestCase

from pydantic import ValidationError

from system.domain.entities.buy_operation_capital_gain_entity import (
    BuyOperationCapitalGainEntity,
)
from system.domain.value_objects.tax_value_object import TaxValueObject


def test_tax_buy_operation_sucess(
    mock_buy_operation: BuyOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_buy_operation.tax.tax_value, Decimal("0.00"))


def test_tax_buy_operation_fail_tax_different_zero() -> None:
    test_case = TestCase()

    with test_case.assertRaises(ValidationError) as error:
        BuyOperationCapitalGainEntity(
            type="buy",
            unit_cost=Decimal("10.00"),
            quantity=10000,
            operations_total_quantity=10000,
            tax=TaxValueObject(value=10, tax_rate=20),
        )

    test_case.assertIn("A Buy Operation doesent have tax", str(error.exception))


def test_calculate_new_weighted_average_price_buy_first_operation_sucess(
    mock_buy_operation_first_operation: BuyOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_buy_operation_first_operation.new_operation_weighted_average_price,
        Decimal("10.00"),
    )


def test_calculate_new_weighted_average_price_buy_not_first_operation_sucess(
    mock_buy_operation: BuyOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        mock_buy_operation.new_operation_weighted_average_price,
        Decimal("15.00"),
    )
