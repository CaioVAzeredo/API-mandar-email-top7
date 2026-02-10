import os
from typing import List
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

def _parse_origins(raw: str) -> List[str]:
    # Ex: "http://localhost:4200,https://top7esportes.com"
    return [o.strip() for o in raw.split(",") if o.strip()]


class Config():
    def _get_env(self, name: str, default: str | None = None) -> str:
        value = os.getenv(name, default)
        if value is None or value.strip() == "":
            raise RuntimeError(f"Missing env var: {name}")
        return value.strip()
    
    def __init__(self):
        self.SMTP_HOST = self._get_env("SMTP_HOST")
        self.SMTP_PORT = int(self._get_env("SMTP_PORT", "587"))
        self.SMTP_USER = self._get_env("SMTP_USER")
        self.SMTP_PASS = self._get_env("SMTP_PASS")

        self.MAIL_FROM = self._get_env("MAIL_FROM")
        self.MAIL_TO = self._get_env("MAIL_TO")

        self.CORS_ORIGINS = _parse_origins(self._get_env("CORS_ORIGINS", "http://localhost:4200"))
