from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from config import ALLOW_ORIGINS, HOST, PORT
from .routers import tricktionary, auth

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(tricktionary.router, prefix="/tricktionary")
app.include_router(auth.router, prefix="/auth")

async def run_api():
    config = Config(
        app=app,
        host=HOST,
        port=PORT,
        timeout_graceful_shutdown=5
    )
    server = Server(config=config)

    await server.serve()
