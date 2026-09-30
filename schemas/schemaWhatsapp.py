#Formato dos dados - Transformação da mensagem

from pydantic import BaseModel

class MessageRequest(BaseModel):
    destino: str
    contato: str
    mensagem: str
    