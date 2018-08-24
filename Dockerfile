FROM python:3.7

ADD ./ /app

WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy --dev
