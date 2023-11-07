FROM python:3.11.4

ENV DB_SERVER=localhost
ENV DB_PORT=5432
ENV DB_DATABASE=postgres
ENV DB_USERNAME=postgres
ENV DB_PASSWORD=postgres
ENV SECRET_KEY=SECRET_KEY

COPY ./requirements.txt ./requirements.txt
COPY ./api.py ./api.py
COPY ./auth ./auth
COPY ./routers ./routers
COPY ./database ./database




RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
