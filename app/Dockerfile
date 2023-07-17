FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY config/requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt
ENV DJANGO_SUPERUSER_USERNAME ahmed
ENV DJANGO_SUPERUSER_PASSWORD Av123456
ENV DJANGO_SUPERUSER_EMAIL ahmed@ahmed.com
RUN pip install -r requirements.txt

COPY . .

# running migrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --noinput  

# gunicorn
CMD ["gunicorn", "--config", "config/gunicorn-cfg.py", "core.wsgi"]
