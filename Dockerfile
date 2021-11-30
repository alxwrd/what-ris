FROM python:3.8

WORKDIR /app

LABEL maintainer="Alex Ward <alxwrd@googlemai.com>"

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./pyproject.toml /app/pyproject.toml

RUN poetry install --no-dev

COPY ./ris /app/ris

CMD ["uvicorn", "ris.api:app", "--host", "0.0.0.0", "--port", "80"]
