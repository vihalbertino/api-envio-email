from fastapi import FastAPI
from services.message import save_message
from services.email import send_email
from schemas.schemaEmail import EmailRequest
from services.automation import create_health_email
from dotenv import load_dotenv
import os
load_dotenv()

destino = os.getenv("EMAIL_DESTINO")
app = FastAPI()


@app.get("/send-health-email")
def send_health_email():

    file_path = r"C:\Users\kelli\OneDrive\Área de Trabalho\script\coleta_aws\aws-health-monitor\tests\fixtures"
    file_name = "sample_currentevents.json"

    assunto, mensagem = create_health_email(
        file_path,
        file_name
    )

    dados = EmailRequest(
        destino=destino,
        assunto=assunto,
        mensagem=mensagem
    )

    send_email(dados)

    save_message(
        f"E-mail AWS Health enviado | destino: {dados.destino}"
    )

    return {"status": "E-mail enviado!"}