from pydantic import BaseModel
from typing import Dict


class habitacionInDB(BaseModel):
    numerohabitacion: str
    estado: bool


database_habitacion = []
database_habitacion = {
    "304","305"
}

def get_habitacion(habitacion: str):
    if habitacion in database_habitacion.keys():
        return database_habitacion[habitacion]
    else:
        return None

