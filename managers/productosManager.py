import psycopg
from models import Producto

class ProductoManager:
    def insertarProducto(self, producto: Producto, cursor: psycopg.Cursor):
        cursor.execute("INSERT INTO productos(nombre, precio)VALUES (%s,%s)",(producto.nombre, producto.precio))
        return "Producto agregado."

    def obtenerProducto(self, cursor: psycopg.Cursor):
        res = cursor.execute("SELECT * FROM productos").fetchall()
        return [{"id_producto": row[0], "nombre": row[1], "precio": row[2]} for row in res]
        