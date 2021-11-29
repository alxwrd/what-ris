

def test_predictions(test_client, iris_test_data):
    features = iris_test_data.get("features")

    response = test_client.get("/predict"
        f"?sepal_length={features[0]}"
        f"&sepal_width={features[1]}"
        f"&petal_length={features[2]}"
        f"&petal_width={features[3]}"
    )

    names = ["setosa", "versicolor", "virginica"]

    assert names[iris_test_data.get("class")] == response.json().get("result")
