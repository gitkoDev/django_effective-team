FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYCODE=1

# RUN pip freeze > requirements.txt
# RUN pip install -r requirements.txt

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


