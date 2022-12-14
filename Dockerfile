# Use an existing docker image as a base
FROM python:3.9-buster

#Change working directory
WORKDIR /app

# COPY requirements.txt
COPY ./requirements.txt ./

RUN pip install -r requirements.txt
# Copy main.py file
COPY ./userSystem ./

RUN  python manage.py collectstatic --noinput

EXPOSE 9000/tcp

# Tell what to do when it starts as a container
CMD ["gunicorn", "userSystem.wsgi:application", "--bind", "0.0.0.0:9000"]
