FROM python:3.10.5-slim-bullseye AS requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.10.5-slim-bullseye

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]