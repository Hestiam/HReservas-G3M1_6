from pydantic import BaseModel
from typing import Dict


class habitacionInDB(BaseModel):
    numerohabitacion: str
    estado: bool


database_habitacion = []
database_habitacion = {
    "304","305","306","307"
}

def get_habitacion(habitacion: str):
    if habitacion in database_habitacion:
        return database_habitacion[habitacion]
    else:
        return None

