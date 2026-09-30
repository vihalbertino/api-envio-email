from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_LOG = BASE_DIR / "mensagens.txt"

def save_message(mensagem: str):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("mensagens.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data_hora}] {mensagem}\n")