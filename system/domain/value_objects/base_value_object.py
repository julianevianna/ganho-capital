from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

from pydantic import BaseModel, validator


class BaseValueObject(BaseModel):
    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True
        validate_assignment = True

    @validator("*", pre=True)
    def validate_decimals(cls, v):
        if isinstance(v, Decimal):
            try:
                return Decimal(v).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
            except InvalidOperation:
                raise ValueError("Invalid Decimal value")
        return v
