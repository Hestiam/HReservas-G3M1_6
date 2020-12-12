import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from Modules import clientes_modules
from Modules import reserva_modules
from Database import clientes_db
from Database import habitaciones_db
from Database import reserva_db

api = FastAPI()


@api.get("/clientes/{cedula}")
async def get_cliente(cedula: str):
    cliente_in_db = clientes_db.get_cliente(cedula)
    if cliente_in_db == None:
        raise HTTPException(
            status_code=404, detail="El cliente no se encuentra registrado")
    cliente_out = clientes_modules.ClienteOut(**cliente_in_db.dict())
    return cliente_out


@api.post("/reserva/")
async def create_reserva(reserva_to_db: reserva_modules.ReservaIn):
    reserva_db.save_reserva(reserva_to_db)
    return reserva_to_db,"creada"
