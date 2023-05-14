from pydantic import BaseModel, Extra


class Input(BaseModel, extra=Extra.forbid):
    """Base schema for inputs"""
