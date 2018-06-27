FROM python:2.7.11
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /opt/requirements/requirements.txt
RUN pip install -r /opt/requirements/requirements.txt
WORKDIR /opt/project


