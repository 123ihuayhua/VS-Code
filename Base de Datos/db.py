import mysql.connector

# Datos de conexión a la base de datos
host = 'localhost'
port = 3306
user = 'root'
password = 'lm10kayca'
database = 'hotel'

# Función para establecer la conexión a la base de datos
def establecer_conexion():
    try:
        conexion = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        # La conexión se realizó con éxito
        print("Conexión exitosa a la base de datos.")
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Función para cerrar la conexión a la base de datos
def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")
