from pydantic import BaseModel

class ClienteIn(BaseModel):
    cedula: str
    nombre: str
    email: str

    
class ClienteOut(BaseModel):
    nombre: str
    email: str