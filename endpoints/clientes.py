from fastapi import APIRouter,Depends
import psycopg
from managers.conexionManagerSupaBase import getCursor
from models import Cliente
from db.db import DB

db = DB()

router=APIRouter(prefix="/clientes", tags=["Clientes routers"])

@router.post("/crear_cliente")
async def crear_cliente(cliente: Cliente, cursor:psycopg.Cursor=Depends(getCursor)):
    res = db.InsertarCliente(cliente, cursor)
    return res

@router.get("/obtener_clientes")
async def obtener_cliente(cursor:psycopg.Cursor=Depends(getCursor)):
    res= db.ObtenerCliente(cursor)
    return res