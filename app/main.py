from fastapi import FastAPI
from app.routes.clients import router as clients_router

app = FastAPI()

app.include_router(clients_router)
