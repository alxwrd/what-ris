
from enum import Enum
from typing import List
from pydantic import BaseModel


class IrisData(BaseModel):
    sepal_length: float = 0.0
    sepal_width: float = 0.0
    petal_length: float = 0.0
    petal_width: float = 0.0


class IrisResult(str, Enum):
    SETOSA = "setosa"
    VERSICOLOR = "versicolor"
    VIRGINICA = "virginica"


class IrisResponse(BaseModel):
    result: List[IrisResult]
