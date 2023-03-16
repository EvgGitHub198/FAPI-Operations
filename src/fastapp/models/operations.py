from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class OperationType(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class BaseOperation(BaseModel):
    data: date
    type: OperationType
    amount: Decimal
    description: Optional[str]


class Operation(BaseOperation):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(BaseOperation):
    pass


class OperationUpdate(BaseOperation):
    pass
