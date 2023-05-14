from decimal import Decimal
from unittest import TestCase

from system.domain.entities.buy_operation_capital_gain_entity import (
    BuyOperationCapitalGainEntity,
)


def test_tax_buy_operation_sucess(
    mock_buy_operation: BuyOperationCapitalGainEntity,
) -> None:
    test_case = TestCase()

    test_case.assertEqual(mock_buy_operation.tax.tax_value, Decimal("0.00"))
