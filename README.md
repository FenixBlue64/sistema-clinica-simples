# 🏥 Sistema de Agendamento de Consultas (Python)

Este projeto é um **sistema simples de agendamento de consultas médicas**, desenvolvido em **Python**, utilizando apenas recursos básicos da linguagem.  
O objetivo principal foi **praticar lógica de programação**, estruturas de controle e manipulação de arquivos.

> Este é meu **primeiro código publicado no GitHub**, focado em aprendizado e evolução contínua.

---

## 🚀 Funcionalidades

O sistema funciona via **terminal** e permite:

- 📅 **Agendar até 4 consultas**
- 📋 **Listar consultas agendadas**
- ❌ **Cancelar consultas**
- 💾 **Salvar consultas em arquivo (`Consultas.txt`)**
- 📖 **Ler consultas salvas anteriormente**
- 🗑️ **Apagar consultas salvas**
- 🚪 **Sair do sistema com opção de salvar os dados**

---

## 🧠 Conceitos de Python Utilizados

Neste projeto foram aplicados:

- Variáveis e listas
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while`)
- Tratamento de erros (`try / except`)
- Manipulação de arquivos (`open`, leitura e escrita)
- Entrada e saída de dados (`input`, `print`)
- Organização lógica de um menu interativo

---

## ⏰ Horários Disponíveis para Consulta

O sistema permite escolher entre os seguintes horários:

- `12:00`
- `14:30`
- `17:00`

---

## 🩺 Especialidades Disponíveis

- Clínica Geral  
- Pediatria  
- Ginecologia  
- Cardiologia  
- Dermatologia  

*(A especialidade é digitada pelo usuário no momento do agendamento)*

---

## 📁 Estrutura do Projeto

```text
📦 sistema-agendamento
 ┣ 📜 sistema-clinicas.py
 ┣ 📄 Consultas.txt   (gerado pelo sistema)
 ┗ 📘 README.md
