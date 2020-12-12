from datetime import datetime
from pydantic import BaseModel

class ReservaInDB(BaseModel):
    id_reserva: int 
    habitacion: str
    cliente: str
    fecha_reserva: datetime = datetime.now()
    
database_reserva = []
generator = {"id":0}

def save_reserva(reserva_in_db: ReservaInDB):
    generator["id"] = generator["id"] + 1
    reserva_in_db.id_reserva = generator["id"]
    database_reserva.append(reserva_in_db)
    return reserva_in_db