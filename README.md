# API-mandar-email-top7

API desenvolvida em Java que permite o envio de mensagens por email para destinatários específicos do grupo Top7.

*Tecnologias*

-Java 17+
-Spring Boot
-Spring Mail (JavaMailSender)
-Maven

*Funcionalidades*

-Envio de e-mails personalizados via requisição HTTP POST.

*Configure seu arquivo application.properties ou application.yml:*

spring.mail.host=smtp.gmail.com
spring.mail.port=587
spring.mail.username=seu-email@gmail.com
spring.mail.password=sua-senha
spring.mail.properties.mail.smtp.auth=true
spring.mail.properties.mail.smtp.starttls.enable=true


#Como usar

POST /api/email

*Exemplo de JSON:*

{
  "assunto": "Assunto do Email",
  "email": "email@exemplo.com",
  "mensagem": "Conteúdo da mensagem"
}
*Resposta de sucesso:*
{
  "message": "Email enviado com sucesso!"
}
