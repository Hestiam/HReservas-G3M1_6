from pydantic import BaseModel

class ClienteIn(BaseModel):
    cedula: str
    
class ClienteOut(BaseModel):
    nombre: str
    email: str