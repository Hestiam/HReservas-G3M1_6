from typing import Dict
from pydantic import BaseModel

class clientInDB(BaseModel):
    cedula: str
    nombre: str
    email: str
    

database_clientes = Dict[str, clientInDB]
database_clientes = {
    "79332654": clientInDB(**{"cedula":"79332654","nombre":"camilo sanchez",
    "email":"camsam45@gmail.com",
    }),
    "64558794": clientInDB(**{"cedula":"64558794","nombre":"Andrea Barrera",
    "email":"barrera65@hotmail.com",
    }),
}

def get_clientes():
        return database_clientes
   
def get_cliente(cedula: str):
    if cedula in database_clientes.keys():
     return database_clientes[cedula]
    else:
        return None

def save_cliente(cliente_in_db: clientInDB):
    database_clientes[cliente_in_db.cedula]= cliente_in_db
    return cliente_in_db