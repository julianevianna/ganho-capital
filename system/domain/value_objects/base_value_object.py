from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

from pydantic import BaseModel, root_validator


class BaseValueObject(BaseModel):
    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True
        validate_assignment = True

    @root_validator(pre=True)
    def validate_decimals(cls, values):
        for index, value in values.items():
            if isinstance(values[index], Decimal):
                try:
                    values[index] = Decimal(value).quantize(
                        Decimal("0.00"),
                        rounding=ROUND_HALF_UP,
                    )
                except InvalidOperation:
                    raise ValueError("Invalid Decimal value")
        return values
