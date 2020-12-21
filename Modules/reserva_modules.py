from pydantic import BaseModel
from datetime import datetime

class ReservaIn(BaseModel):
    id_reserva: int 
    habitacion: str
    cliente: str
    fecha_reserva: datetime = datetime.now()
    
    
    
class ReservaOut(BaseModel):
    habitacion: str
    cliente: str