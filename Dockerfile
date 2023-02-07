FROM python:3.10.9-alpine3.17
RUN mkdir -p /tmp/musiclibraly
WORKDIR /tmp/musiclibraly
COPY . /tmp/musiclibraly
RUN pip install uvicorn gunicorn
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ EUROPE/MOSCOW
RUN python manage.py makemigrations library && python manage.py migrate
CMD  gunicorn --bind :8000 --workers 3 core.wsgi:application 
