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
    habita = reserva_in_db[habitacion]
    dhabitacion=database_habitacion[habita]["disponible"]
    if dhabitacion == True:
        generator["id"] = generator["id"] + 1
        reserva_in_db.id_reserva = generator["id"]
        database_reserva.append(reserva_in_db)
        return reserva_in_db
    else :
        mensaje= "Lo sentimos la habitacion ya esta reservada"
        print(mensaje)
        return None

def get_reserva(id_reserva: int):
    if reserva in database_reserva.keys():
     return database_reserva[reserva]
    else:
        return None