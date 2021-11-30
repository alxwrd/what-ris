
from typing import Optional, List, Union

from fastapi import FastAPI, HTTPException, Depends

from ris.schemas.iris import IrisData, IrisResponse
from ris.services.iris import iris_predictor, IrisPredictor

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


@app.post("/predict", response_model=IrisResponse)
def predict_iris(
    iris: Union[IrisData, List[IrisData]],
    predictor: IrisPredictor = Depends(iris_predictor)
):
    if isinstance(iris, IrisData):
        iris = [iris]

    return {"result": predictor.predict(iris)}
