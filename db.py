import psycopg
from models import Cliente, Producto, Pedido
from dotenv import load_dotenv

class DB:




    def InsertarCliente(self, cliente: Cliente,cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO clientes (nombre, telefono)VALUES (%s,%s)", (cliente.nombre, cliente.telefono))
        return {"msg" : "Cliente creado."}
    

    
    def ObtenerCliente(self, cursor:psycopg.Cursor):
        cursor.execute("SELECT * FROM clientes")
        res=cursor.execute ("SELECT id_clientes, nombre FROM clientes").fetchall()
        return [{"id": row [0], "nombre":row [1]} for row in res]
    

    def InsertarProducto(self, producto: Producto,cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO productos(nombre, precio)VALUES (%s,%s)",(producto.nombre, producto.precio))
        return {"msg" : "Producto creado."}
    
    def ObtenerProductos(self, cursor: psycopg.Cursor):
        cursor.execute("SELECT * FROM productos")
        columnas = [desc[0] for desc in cursor.description]
        return [dict(zip(columnas, row)) for row in cursor.fetchall()]


    def InsertarPedido(self, pedido: Pedido,cursor:psycopg.Cursor):
        cursor.execute("INSERT INTO pedidos(cliente_id, producto_id, cantidad)VALUES (%s,%s,%s)",(pedido.cliente_id, pedido.producto_id, pedido.cantidad))
        return {"msg" : "Pedido creado."}

    
    def ObtenerPedidos(self):
        cursor = self.conn.cursor() 
        cursor.execute("SELECT * FROM pedidos")
        resultado = cursor.fetchall()   
        cursor.close()              
        return resultado