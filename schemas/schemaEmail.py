#Formato dos dados - Transformação da mensagem
from pydantic import BaseModel

class EmailRequest(BaseModel):
    destino: str
    assunto: str
    mensagem: str