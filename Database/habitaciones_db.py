from pydantic import BaseModel
from typing import Dict


class habitacionInDB(BaseModel):
    numerohabitacion: str
    disponible: bool
    camas: int
    detalles: str


database_habitacion = Dict[str,habitacionInDB]
database_habitacion = {
    "304": habitacionInDB(**{"numerohabitacion":"304","disponible":"True","camas": 3,"detalles": "Vista al mar"}),
    "305": habitacionInDB(**{"numerohabitacion":"305","disponible":"False","camas": 2,"detalles": "Aire acondicionado"}),
    "306": habitacionInDB(**{"numerohabitacion":"306","disponible":"False","camas": 4,"detalles": "Television con recepción satelital"}),
}

def get_habitacion(habitacion: str):
    if habitacion in database_habitacion.keys():
        return database_habitacion[habitacion]
    else:
        return None

