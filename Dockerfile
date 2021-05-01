FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT FLASK_APP=app.py FLASK_ENV=development flask run --host=0.0.0.0