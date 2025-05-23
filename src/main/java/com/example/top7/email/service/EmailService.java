package com.example.top7.email.service;

import com.example.top7.email.dto.ContatoDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class EmailService {

    @Autowired
    private JavaMailSender mailSender;

    public void enviarEmail(ContatoDTO dto) {
        SimpleMailMessage mensagem = new SimpleMailMessage();
        mensagem.setFrom("enviaremail698@gmail.com");
        mensagem.setTo("caio.viana.39@gmail.com");
        mensagem.setSubject("Assunto: " + dto.getAssunto());
        mensagem.setText(
                "Nome: " + dto.getNome() + "\n" +
                        "Email: " + dto.getEmail() + "\n" +
                        "mensagem: " + dto.getMensagem() + "\n"
        );

        mailSender.send(mensagem);
    }
}
