from app.config import Config
from app.schemas.contato_schema import ContatoPayload
from app.routers.health import router as health_router
from app.routers.contato import router as contato_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


config = Config()

app = FastAPI(title="API Contato - Envio de Email")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(contato_router)