from fastapi import FastAPI

from endpoints.clientes import router as clientes_router
from endpoints.productos import router as productos_router
from endpoints.pedidos import router as pedidos_router

app = FastAPI()

app.include_router(clientes_router)
app.include_router(productos_router)
app.include_router(pedidos_router)