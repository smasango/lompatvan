FROM python:3.11.1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy requirements file to host
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput