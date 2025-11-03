import psycopg
from models import Pedido

class PedidosManager:
    def obtenerPedidos(self, cursor: psycopg.Cursor):
        res = cursor.execute("SELECT pedidos.pedido_id,clientes.nombre AS cliente,productos.nombre AS producto,productos.precio,pedidos.cantidad,(productos.precio * pedidos.cantidad) AS total FROM pedidos INNER JOIN clientes ON pedidos.cliente_id = clientes.id_clientes INNER JOIN productos ON pedidos.producto_id = productos.producto_id").fetchall()
        return [
            {"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res
        ]

    def insertarPedido(self, pedido: pedido, cursor: psycopg.Cursor):
        cursor.execute ("INSERT INTO pedidos(clientes_id, producto_id, cantidad)VALUES (%s,%s,%s)",(pedido.cliente_id, pedido.producto_id, pedido.cantidad))
        return "Pedido agregado."