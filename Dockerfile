FROM python:3.11

ENV PIP_DEFAULT_TIMEOUT=100 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_NO_CACHE_DIR=1 

RUN mkdir /app

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --without dev

COPY . /app/

EXPOSE 8000

CMD ["poetry","run","uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

