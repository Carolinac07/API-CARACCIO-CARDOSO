from fastapi import APIRouter
from models import Cliente
from db.db import DB

db = DB()

router=APIRouter(prefix="/clientes", tags=["Clientes routers"])

@router.post("/crear_cliente")
async def crear_cliente(cliente: Cliente):
    res = db.InsertarCliente(cliente)
    return res

@router.get("/obtener_clientes")
async def obtener_cliente():
    res= db.ObtenerCliente()
    return res