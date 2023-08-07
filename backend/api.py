from fastapi import FastAPI
from routers import get_tables
from routers import health_check
from routers import root
from routers import auth

app = FastAPI()

app.include_router(root.router)
app.include_router(health_check.router)
app.include_router(get_tables.router)
app.include_router(auth.router)