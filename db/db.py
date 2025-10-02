import sqlite3
from models import Cliente, Producto, Pedido
from dotenv import load_dotenv

class DB:
    def __init__(self):
        self.conn=sqlite3.connect("test.db")
        self.conn.row_factory=sqlite3.Row
        self.cursor=self.conn.cursor()
        self.init_db() 

    def init_db(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS clientes(id_cliente INTEGER PRIMARY KEY,nombre TEXT,telefono INT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS productos(producto_id INTEGER PRIMARY KEY,nombre TEXT,precio INT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS pedidos(pedido_id INTEGER PRIMARY KEY,cliente_id INTEGER,producto_id INTEGER,cantidad INTEGER,FOREIGN KEY (cliente_id) REFERENCES clientes (id_cliente) FOREIGN KEY (producto_id) REFERENCES productos (producto_id))")
        self.conn.commit()
    

    def InsertarCliente(self, cliente: Cliente):
        self.conn.execute("INSERT INTO clientes (nombre, telefono)VALUES (?,?)", (cliente.nombre, cliente.telefono))
        self.conn.commit()
        return {"msg" : "Cliente creado."}
    
    def ObtenerCliente(self):
        self.cursor.execute("SELECT * FROM clientes")
        return [dict(row) for row in self.cursor.fetchall()]
    

    def InsertarProducto(self, producto: Producto):
        self.conn.execute("INSERT INTO productos(nombre, precio)VALUES (?,?)",(producto.nombre, producto.precio))
        self.conn.commit()
        return {"msg" : "Producto creado."}
    
    def ObtenerProductos(self):
        self.cursor.execute("SELECT * FROM productos")
        return [dict(row) for row in self.cursor.fetchall()]


    def InsertarPedido(self, pedido: Pedido):
        self.conn.execute("INSERT INTO pedidos(cliente_id, producto_id, cantidad)VALUES (?,?,?)",(pedido.cliente_id, pedido.producto_id, pedido.cantidad))
        self.conn.commit()
        return {"msg" : "Pedido creado."}
    
    def ObtenerPedidos(self):
        self.cursor.execute("""
            SELECT 
                pedidos.pedido_id,
                clientes.nombre AS cliente,
                productos.nombre AS producto,
                productos.precio,
                pedidos.cantidad,
                (productos.precio * pedidos.cantidad) AS total
            FROM pedidos
            INNER JOIN clientes ON pedidos.cliente_id = clientes.id_cliente
            INNER JOIN productos ON pedidos.producto_id = productos.producto_id
        """)
        return [dict(row) for row in self.cursor.fetchall()]