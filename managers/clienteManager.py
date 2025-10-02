import psycopg
from models import Cliente

class ClienteManager:
    def addClient(self, cliente:Cliente, cursor:psycopg.Cursor):
        cursor.execute(
            "INSERT INTO cliente (nombre, telefono) VALUES (%s)",
            (cliente.nombre, cliente.telefono),
        )
        return f"cliente creado"

    def getClientes(self, cursor:psycopg.Cursor)-> list:
        res=cursor.execute ("SELECT id_cliente, nombre FROM cliente").fetchall()
        return [{"id": row [0], "nombre":row [1]} for row in res]
    