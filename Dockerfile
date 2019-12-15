FROM python:3.6-alpine
WORKDIR /code
COPY . .
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt --no-cache-dir && \
    pip install gunicorn --no-cache-dir
ENV FLASK_APP run.py
#ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000
CMD flask run --host=0.0.0.0