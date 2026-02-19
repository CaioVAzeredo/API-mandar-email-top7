# API-mandar-email-top7

API desenvolvida em Python com FastAPI que permite o envio de mensagens por e-mail para destinatários específicos do grupo Top7.

# Tecnologias

Python 3.10+ (recomendado 3.11+)

FastAPI

Uvicorn (servidor ASGI)

Pydantic (validação do JSON)

# Envio de e-mail via SMTP (smtplib + email.message)

(Opcional) python-dotenv para carregar variáveis de ambiente via .env

# Funcionalidades

Envio de e-mails personalizados via requisição HTTP POST.

Validação dos dados de entrada (assunto, e-mail do destinatário e mensagem).

# Configuração

Crie variáveis de ambiente (recomendado) — exemplo usando Gmail SMTP:

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu-email@gmail.com
SMTP_PASS=sua-senha-ou-senha-de-app


# Importante (Gmail): normalmente você precisa usar Senha de App (com verificação em duas etapas ativada), não a senha normal da conta.

Se você usa .env, coloque esse arquivo na raiz do projeto e carregue no código (caso já esteja configurado no seu projeto).

# Como rodar o projeto

Instale as dependências:

pip install -r requirements.txt

Suba a API:

uvicorn app.main:app --host 0.0.0.0 --port 8000

# Como usar
Enviar e-mail

POST /api/email

Exemplo de JSON
{
  "assunto": "Assunto do Email",
  "email": "email@exemplo.com",
  "mensagem": "Conteúdo da mensagem"
}

Resposta de sucesso
{
  "message": "Email enviado com sucesso!"
}

# Observações

Se os e-mails estiverem caindo no spam, isso pode acontecer por reputação do remetente, conteúdo da mensagem e configurações do domínio/provedor.


