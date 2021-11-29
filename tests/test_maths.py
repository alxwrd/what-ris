

from fastapi.testclient import TestClient


def test_summing_two_numbers(test_client: TestClient):
    response = test_client.get("/sum?a=1&b=1")

    assert response.json().get("result") == 2


def test_summing_two_non_numbers(test_client: TestClient):
    response = test_client.get("/sum?a=foo&b=bar")

    assert response.status_code == 422

    for error_detail in response.json().get("detail"):
        assert error_detail.get("msg") == "value is not a valid integer"


def test_summing_one_number_a(test_client: TestClient):
    response = test_client.get("/sum?a=42")

    assert response.json().get("result") == 42


def test_summing_one_number_b(test_client: TestClient):
    response = test_client.get("/sum?b=9001")

    assert response.json().get("result") == 9001


def test_dividing_two_numbers(test_client: TestClient):
    response = test_client.get("/div?a=1&b=1")

    assert response.json().get("result") == 1


def test_dividing_two_non_numbers(test_client: TestClient):
    response = test_client.get("/div?a=spam&b=eggs")

    assert response.status_code == 422

    for error_detail in response.json().get("detail"):
        assert error_detail.get("msg") == "value is not a valid integer"


def test_dividing_by_zero(test_client: TestClient):
    response = test_client.get("/div?a=1000&b=0")

    assert response.status_code == 422

    response.json().get("detail") == "cannot divide by zero"


def test_dividing_no_b_number(test_client: TestClient):
    response = test_client.get("/div?a=1000")

    assert response.status_code == 422

    response.json().get("detail") == "undefined behaviour"


def test_dividing_no_a_number(test_client: TestClient):
    response = test_client.get("/div?b=1000")

    assert response.status_code == 422

    response.json().get("detail") == "undefined behaviour"
