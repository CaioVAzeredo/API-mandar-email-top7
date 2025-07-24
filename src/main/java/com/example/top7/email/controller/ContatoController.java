package com.example.top7.email.controller;

import com.example.top7.email.dto.ContatoDTO;
import com.example.top7.email.service.EmailService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/contato")
@CrossOrigin(origins = "*")
public class ContatoController {
    @Autowired
    private EmailService emailService;

    @PostMapping
    public ResponseEntity<Map<String, String>> enviar(@RequestBody ContatoDTO dto) {
        emailService.enviarEmail(dto);

        Map<String, String> resposta = new HashMap<>();
        resposta.put("mensagem", "E-mail enviado com sucesso!!");

        return ResponseEntity.ok(resposta);
    }

    @GetMapping
    public String testar() {
        return "API Funcionando";
    }

}
