from fastapi import APIRouter
from models import Producto
from db.db import DB

db = DB()
router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/crear_producto")
async def crear_producto(producto: Producto):
    return db.InsertarProducto(producto)

@router.get("/obtener_productos")
async def obtener_productos():
    return db.ObtenerProductos()