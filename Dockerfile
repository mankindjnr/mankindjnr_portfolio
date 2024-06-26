FROM python:3.10.12

WORKDIR /portfolio

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]