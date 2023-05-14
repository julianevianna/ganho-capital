from pydantic import BaseModel


class BaseValueObject(BaseModel):
    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        use_enum_values = True
        arbitrary_types_allowed = True
        validate_assignment = True
