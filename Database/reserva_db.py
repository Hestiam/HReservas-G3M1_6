from datetime import datetime
from pydantic import BaseModel
from Database.habitaciones_db import database_habitacion

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

def get_reserva(id_reserva: int):
    if reserva in database_reserva.keys():
     return database_reserva[reserva]
    else:
        return None