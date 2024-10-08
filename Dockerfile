FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

# ENV FASTAPI_ENV="production"

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
