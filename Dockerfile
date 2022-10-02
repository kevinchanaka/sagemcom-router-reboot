FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

CMD ["python", "main.py"]
