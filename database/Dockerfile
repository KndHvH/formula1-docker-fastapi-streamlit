FROM postgres:15

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres

COPY ./data ./data

COPY ./01_CREATE_DB.sql /docker-entrypoint-initdb.d/
COPY ./02_COPY_DATA.sql /docker-entrypoint-initdb.d/