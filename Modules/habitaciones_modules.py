from pydantic import BaseModel

class HabitacionIn(BaseModel):
    numerohabitacion: str
    
    
class HabitacionOut(BaseModel):
    numerohabitacion: str
    camas:int
    detalles: str