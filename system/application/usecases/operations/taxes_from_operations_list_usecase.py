from decimal import Decimal

from system.application.dto.operation_list_input import OperationsListInput
from system.application.dto.taxes_list_output import TaxesListOutput
from system.application.enums.operation_type_enum import OperationTypeEnum
from system.application.usecases.usecase import UseCase
from system.domain.entities.buy_operation_capital_gain_entity import (
    BuyOperationCapitalGainEntity,
)
from system.domain.entities.operation_capital_gain_entity import (
    OperationCapitalGainEntity,
)
from system.domain.entities.operation_entity import OperationEntity
from system.domain.entities.operation_list_entity import OperationListEntity
from system.domain.entities.sell_operation_capital_gain_entity import (
    SellOperationCapitalGainEntity,
)


class TaxesFromOperationsListUsecase(UseCase):
    def execute(
        self,
        input_usecase: OperationsListInput,
    ) -> TaxesListOutput:
        operation_list_entity = OperationListEntity(operations=[])
        operations_total_quantity: int = 0
        operation_weighted_average_price: Decimal = Decimal("0.00")
        previous_loss: Decimal = Decimal("0.00")

        for operation in input_usecase.operation_list:
            operation_entity = OperationEntity(**operation.dict())
            operation_capital_gain_entity: OperationCapitalGainEntity = (
                self.create_operation_capital_gain_by_type(
                    operation_entity.type,
                    operation_entity,
                    operations_total_quantity,
                    operation_weighted_average_price,
                    previous_loss,
                )
            )
            operation_list_entity.operations.append(operation_capital_gain_entity)

            operations_total_quantity = (
                operation_capital_gain_entity.new_operations_total_quantity
            )
            operation_weighted_average_price = (
                operation_capital_gain_entity.new_operation_weighted_average_price
            )

            previous_loss = (
                self.calculate_loss(
                    previous_loss,
                    operation_capital_gain_entity.returns.returns,  # type: ignore
                )
                if operation_capital_gain_entity.type == OperationTypeEnum.SELL.value
                else previous_loss
            )

        return TaxesListOutput(
            taxes=list(
                map(
                    lambda operation: operation.tax.tax_value,
                    operation_list_entity.operations,
                ),
            ),
        )

    @staticmethod
    def create_operation_capital_gain_by_type(
        type: OperationTypeEnum,
        operation_entity: OperationEntity,
        operations_total_quantity: int = 0,
        operation_weighted_average_price: Decimal = Decimal("0.00"),
        previous_loss: Decimal = Decimal("0.00"),
    ):
        operation_capital_gain_entity = {
            "buy": BuyOperationCapitalGainEntity(
                unit_cost=operation_entity.unit_cost,
                quantity=operation_entity.quantity,
                operations_total_quantity=operations_total_quantity,
                operation_weighted_average_price=operation_weighted_average_price,
            ),  # type: ignore
            "sell": SellOperationCapitalGainEntity(
                unit_cost=operation_entity.unit_cost,
                quantity=operation_entity.quantity,
                operations_total_quantity=operations_total_quantity,
                operation_weighted_average_price=operation_weighted_average_price,
                previous_loss=previous_loss,
            ),  # type: ignore
        }

        return operation_capital_gain_entity[type]  # type: ignore

    @staticmethod
    def calculate_loss(
        previous_loss: Decimal = Decimal("0.00"),
        returns_value: Decimal = Decimal("0.00"),
    ):
        if returns_value < 0:
            previous_loss = -returns_value
        elif previous_loss > 0 and returns_value > 0:
            previous_loss -= returns_value
        else:
            previous_loss = Decimal("0.00")

        return previous_loss
