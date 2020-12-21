from pydantic import BaseModel

class HabitacionIn(BaseModel):
    numerohabitacion: str
    camas:int
    detalles: str
    
class HabitacionOut(BaseModel):
    numerohabitacion: str
    camas:int
    detalles: str