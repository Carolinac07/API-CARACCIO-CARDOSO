from fastapi import APIRouter, Depends
import psycopg
from managers.conexionManagerSupaBase import getCursor
from models import Producto
from db.db import DB

db = DB()
router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/crear_producto")
async def crear_producto(producto: Producto, cursor:psycopg.Cursor=Depends(getCursor)):
    return db.InsertarProducto (producto,cursor)

@router.get("/obtener_productos")
async def obtener_productos(cursor:psycopg.Cursor=Depends(getCursor)):
    return db.ObtenerProductos(cursor)