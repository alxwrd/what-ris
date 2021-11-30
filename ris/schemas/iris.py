
from pydantic import BaseModel


class IrisData(BaseModel):
    sepal_length: float = 0.0
    sepal_width: float = 0.0
    petal_length: float = 0.0
    petal_width: float = 0.0
