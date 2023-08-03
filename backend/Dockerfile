FROM python:3.11.4

COPY ./api.py ./api.py
COPY ./routers ./routers
COPY ./database ./database
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
