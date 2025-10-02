from fastapi import APIRouter
from models import Pedido
from db.db import DB

db = DB()

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/crear_pedidos")
async def crear_pedido(pedido: Pedido):
    return db.InsertarPedido(pedido)

@router.get("/obtener_pedidos")
async def obtener_pedido():
    return db.ObtenerPedidos()