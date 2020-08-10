FROM python:3.5-alpine

# This only if you are using PostgreSQL
RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev

ADD . /django-realworld-example-app

WORKDIR /django-realworld-example-app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]