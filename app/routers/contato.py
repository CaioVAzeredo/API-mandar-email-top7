from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.schemas.contato_schema import ContatoPayload
from app.services.email_service import enviar_email_smtp

router = APIRouter(tags=["contato"])

@router.post("/api/contato")
def contato(payload: ContatoPayload, background: BackgroundTasks):
    try:
        background.add_task(enviar_email_smtp, payload)
        return {"message": "Recebido! Seu e-mail foi encaminhado com sucesso."}
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao processar o envio.")
