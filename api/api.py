from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from config import ALLOW_ORIGINS, HOST, PORT
from .routers.tricktionary import router as tricktionary_router
from .routers.auth import router as auth_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(tricktionary_router, prefix="/tricktionary")
app.include_router(auth_router, prefix="/auth")

async def run_api():
    config = Config(
        app=app,
        host=HOST,
        port=PORT,
        timeout_graceful_shutdown=5
    )
    server = Server(config=config)

    await server.serve()
