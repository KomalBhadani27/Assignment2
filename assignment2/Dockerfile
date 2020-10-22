FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 5432
EXPOSE 6379
COPY ./load-psql-extension.sh /docker-entrypoint-initdb.d
