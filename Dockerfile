FROM python:3.8

WORKDIR /app

LABEL maintainer="Alex Ward <alxwrd@googlemai.com>"

COPY ./pyproject.toml /app/pyproject.toml

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

ENV PATH="/etc/poetry/bin:${PATH}"

RUN poetry --version
RUN poetry config virtualenvs.create false && \
    python -m pip install numpy==1.21.4 && \
    python -m pip install scipy==1.7.3 && \
    poetry install --no-dev

COPY ./ris /app/ris

ENV PORT=8080
EXPOSE $PORT

CMD ["sh", "-c", "uvicorn ris.api:app --host 0.0.0.0 --port $PORT"]
