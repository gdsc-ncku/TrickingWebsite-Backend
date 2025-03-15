from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from config import ALLOW_ORIGINS, HOST, PORT


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def run_api():
    config = Config(
        app=app,
        host=HOST,
        port=PORT,
        timeout_graceful_shutdown=5
    )
    server = Server(config=config)

    await server.serve()
