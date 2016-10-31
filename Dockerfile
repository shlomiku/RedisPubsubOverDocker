FROM python:2.7.11
ENV PYTHONUNBUFFERED 1


WORKDIR /opt/project
RUN echo "$WORKDIR"
COPY ./ "$WORKDIR"
RUN pip install -r "$WORKDIR"requirements.txt


