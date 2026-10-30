import mysql.connector
from mysql.connector import Error

def conectar_db():
    conexion = None
    try:
        conexion = mysql.connector.connect(
                    host="127.0.0.1",
                    port="3306",
                    user="root",
                    password="gordobubu",
                    database="db_pokes"
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        raise
        
    return conexion