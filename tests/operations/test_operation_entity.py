from decimal import Decimal
from unittest import TestCase

from pydantic import ValidationError

from system.domain.entities.buy_operation_capital_gain_entity import (
    BuyOperationCapitalGainEntity,
)
from system.domain.entities.operation_list_entity import OperationListEntity
from system.domain.entities.sell_operation_capital_gain_entity import (
    SellOperationCapitalGainEntity,
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


def test_weighted_average_price_sucess(
    mock_operations_list_entity: OperationListEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        list(
            map(
                lambda operation: operation.new_operation_weighted_average_price,
                mock_operations_list_entity.operations,
            ),
        ),
        [Decimal("10.00"), Decimal("15.00"), Decimal("15.00")],
    )


def test_operations_total_quantity_sucess(
    mock_operations_list_entity: OperationListEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(
        list(
            map(
                lambda operation: operation.operations_total_quantity,
                mock_operations_list_entity.operations,
            ),
        ),
        [0, 10000, 15000],
    )


def test_tax_sell_operation_profit_sucess(
    mock_sell_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_sell_operation.tax.tax_value, Decimal("0.00"))


def test_tax_sell_operation_loss_sucess(
    mock_sell_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_sell_operation.tax.tax_value, Decimal("0.00"))


def test_tax_sell_operation_zero_sucess(
    mock_sell_operation: SellOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_sell_operation.tax.tax_value, Decimal("0.00"))
