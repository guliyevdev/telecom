FROM python:3.6
MAINTAINER Alvin Aliev,alielvinme@gmail.com
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code
COPY . /code


#RUN apt-get -y update
#RUN apt-get -y upgrade
#RUN apt-get install nano
RUN pip install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --upgrade setuptools
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt
RUN if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi

EXPOSE 8000