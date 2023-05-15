from decimal import Decimal
from unittest import TestCase

from system.domain.entities.operation_list_entity import OperationListEntity


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
