from fastapi import APIRouter, Depends
from managers.conexionManagerSupaBase import getCursor
from models import Pedido
from db.db import DB
import psycopg 

db = DB()

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/crear_pedidos")
async def crear_pedido(pedido: Pedido, cursor:psycopg.Cursor=Depends(getCursor)):
    return db.InsertarPedido(pedido, cursor)


@router.get("/obtener_pedidos")
async def obtener_pedidos():
    return db.ObtenerPedidos()



