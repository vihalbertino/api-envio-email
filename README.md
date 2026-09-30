# API de Envio de Mensagens

API desenvolvida com **FastAPI** para automatizar o envio de notificações por e-mail a partir de dados coletados do **AWS Health**.

O projeto foi criado com foco em automação, organização de código e integração entre serviços.

## 🚀 Tecnologias

- Python
- FastAPI
- Uvicorn
- Pydantic
- Gmail SMTP
- AWS Health
- Git

## 📌 Funcionalidades

- Leitura de eventos do AWS Health em formato JSON
- Estruturação dos dados coletados
- Geração de e-mails em HTML
- Envio de e-mails utilizando Gmail SMTP
- Registro dos envios em arquivo de log
- API REST para execução das automações

## 📂 Estrutura

```text
api-send-message/
├── app/
│   └── main.py
├── routes/
├── schemas/
│   ├── schemaEmail.py
│   └── schemaWhatsapp.py
├── services/
│   ├── automation.py
│
