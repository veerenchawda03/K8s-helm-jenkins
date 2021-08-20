# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim




# COPY ./app /app
# COPY ./requirements.txt /app
# RUN pip3 install pytest
# RUN pip3 install fastapi_health

FROM python:3.9-slim

COPY ./src /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]