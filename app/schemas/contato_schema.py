from typing import Literal
from pydantic import BaseModel, EmailStr, Field

class ContatoPayload(BaseModel):
    assunto: Literal["duvida", "reclamacao", "parceria", "sugestoes", "outro"]
    nome: str = Field(min_length=1, max_length=120)
    email: EmailStr
    mensagem: str = Field(min_length=1, max_length=2000)
