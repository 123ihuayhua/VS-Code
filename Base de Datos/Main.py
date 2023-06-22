from db import *
from Admin import *

# Establecer la conexión a la base de datos
conexion = establecer_conexion()

if conexion is not None:
    # Insertar registros de la tabla turno_admin
    insertar_turno_Admin(conexion, 1, '08:00:00', '14:00:00', 'A')
    # Seleccionar registros de la tabla turno_admin
    seleccionar_turno_admin(conexion)

cerrar_conexion(conexion)