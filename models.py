from pydantic import BaseModel

class Pedido(BaseModel):
    producto_id: int
    cliente_id: int
    cantidad: int

class Cliente(BaseModel):
    nombre: str
    telefono: int

class Producto(BaseModel):
    nombre: str
    precio: int