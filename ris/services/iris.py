
from typing import List

import pickle
import warnings
import pkg_resources


from ris.schemas.iris import IrisData


class IrisPredictor:
    names = ["setosa", "versicolor", "virginica"]

    def __init__(self, model_path: str = None):
        if model_path is None:
            model_path = pkg_resources.resource_filename("ris", "models/iris_model.pkl")

        self.model_path = model_path

        with open(self.model_path, "rb") as f:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=UserWarning)
                self.model = pickle.load(f)

    def predict(self, data: List[IrisData]):
        data_for_model = [
            [
                iris.sepal_length,
                iris.sepal_width,
                iris.petal_length,
                iris.petal_width,
            ] for iris in data
        ]

        return [
            self.names[prediction] for prediction in self.model.predict(data_for_model)
        ]
