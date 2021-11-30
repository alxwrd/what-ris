

def test_predictions(test_client, iris_test_data):
    features = iris_test_data.get("features")

    response = test_client.post("/predict",
        json={
            "sepal_length": features[0],
            "sepal_width": features[1],
            "petal_length": features[2],
            "petal_width": features[3]
        }
    )

    names = ["setosa", "versicolor", "virginica"]

    assert names[iris_test_data.get("class")] == response.json().get("result")[0]


def test_multiple_predictions(test_client, all_validation):
    some_validation = list(all_validation)[:10]

    response = test_client.post("/predict",
        json=[{
            "sepal_length": feature[0],
            "sepal_width": feature[1],
            "petal_length": feature[2],
            "petal_width": feature[3]
        } for klass, feature in some_validation]
    )

    names = ["setosa", "versicolor", "virginica"]

    results = response.json().get("result")

    assert len(results) > 0

    for result, validation in zip(results, some_validation):
        assert names[validation[0]] == result
