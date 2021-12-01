# :hibiscus: What ris?
_What ris_ is an Iris identification service.

## Getting started

### Requires

- Python 3.8+ - https://www.python.org/
- Poetry - https://python-poetry.org/

### Running

To begin: clone this repository, install the dependencies using Poetry,
and run the application using uvicorn.

```shell
git clone git@github.com:alxwrd/what-ris.git
cd what-ris
poetry install
poetry run uvicorn ris.api:app --reload
```

The test suite is written using [pytest](https://docs.pytest.org/en/6.2.x/). To
verify you're ready to go, run the tests:

```shell
$ poetry run pytest
======== test session starts ========
collected 55 items

tests\test_maths.py ........
tests\test_predict.py ..............................................
```


## Documentation

Endpoints are self documenting thanks to FastAPI. After you've started the
application locally, simply visit http://localhost:8000/docs.


## Deployment

Deployed to Google Cloud Platform using:
  - [Container Registry](https://cloud.google.com/container-registry)
  - [Cloud Run](https://cloud.google.com/run)
