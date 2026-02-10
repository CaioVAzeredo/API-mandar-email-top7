from email.message import EmailMessage
import logging
import smtplib

from app.config import Config
from app.schemas.contato_schema import ContatoPayload

config = Config()
logger = logging.getLogger("contato-api")

def enviar_email_smtp(payload: ContatoPayload) -> None:
    msg = EmailMessage()
    msg["From"] = config.MAIL_FROM
    msg["To"] = config.MAIL_TO
    msg["Subject"] = f"[Contato - {payload.assunto}] {payload.nome}"

    corpo = (
        f"Novo contato recebido pelo site.\n\n"
        f"Assunto: {payload.assunto}\n"
        f"Nome: {payload.nome}\n"
        f"E-mail: {payload.email}\n\n"
        f"Mensagem:\n{payload.mensagem}\n"
    )
    msg.set_content(corpo)

    try:
        with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT, timeout=20) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(config.SMTP_USER, config.SMTP_PASS)
            smtp.send_message(msg)

        logger.info("Email enviado com sucesso para %s", config.MAIL_TO)

    except Exception as e:
        logger.exception("Falha ao enviar e-mail: %s", str(e))
        raise