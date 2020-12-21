from fastapi.middleware.cors import CORSMiddleware
import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from Modules import clientes_modules
from Modules import reserva_modules
from Modules import habitaciones_modules
from Database import clientes_db
from Database import habitaciones_db
from Database import reserva_db

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


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
    return reserva_to_db, "creada"


@api.post("/clientes/nuevo_cliente")
async def create_cliente(cliente_to_db: clientes_modules.ClienteIn):
    clientes_db.save_cliente(cliente_to_db)
    return cliente_to_db, "Agregado satisfactoriamente"


@api.get("/habitacion/{numero}")
async def get_habitacion(numero: str):
    habitacion_in_db = habitaciones_db.get_habitacion(numero)
    if habitacion_in_db == None:
        raise HTTPException(
            status_code=404, detail="La habitación no se encuentra registrada")
    habitacion_out = habitaciones_modules.HabitacionOut(**habitacion_in_db.dict())
    return habitacion_out