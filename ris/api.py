
from typing import Optional

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/sum")
def sum_numbers(a: Optional[int] = 0, b: Optional[int] = 0):
    return {"result": a + b}


@app.get("/div")
def div_numbers(a: Optional[int] = None, b: Optional[int] = None):
    if a is None or b is None:
        raise HTTPException(status_code=422, detail="undefined behaviour")

    if a == 0 or b == 0:
        raise HTTPException(status_code=422, detail="cannot divide by zero")

    return {"result": a / b}


@app.get("/predict")
def predict_iris(
    sepal_length: Optional[float] = 0.0,
    sepal_width: Optional[float] = 0.0,
    petal_length: Optional[float] = 0.0,
    petal_width: Optional[float] = 0.0,
):
    return {"result": "setosa"}
