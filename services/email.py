import smtplib
from email.message import EmailMessage
from schemas.schemaEmail import EmailRequest
from dotenv import load_dotenv
import os

load_dotenv()

gmail = os.getenv("EMAIL")
gmail_password = os.getenv("EMAIL_KEY")


def send_email(dados: EmailRequest):
    print("INICIANDO ENVIO")

    email = EmailMessage()
    email["From"] = gmail
    email["To"] = dados.destino
    email["Subject"] = dados.assunto
    email.set_content(dados.mensagem)
    email.add_alternative(dados.mensagem, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        print("CONECTANDO AO GMAIL")
        smtp.login(gmail, gmail_password)
        print("LOGIN OK")
        smtp.send_message(email)
        print("EMAIL ENVIADO")