FROM python:3.8.1-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && \
    apk add --no-cache --virtual build-deps \
    openssl-dev libffi-dev gcc python3-dev musl-dev g++ postgresql-dev netcat-openbsd \
    curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"


WORKDIR /code
COPY . /code/

COPY pyproject.toml poetry.lock ./code/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi


RUN ["chmod", "+x", "/code/entrypoint.sh"]
