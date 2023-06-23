from db import *
from Huesped import *

# Establecer la conexión a la base de datos
conexion = establecer_conexion()

if conexion is not None:
    #INSERT HUESPED
    codigo = 234510
    DNI = "74768625"
    apellido_paterno = "Moroccoire"
    apellido_materno = "Pacompia"
    nombre = "Anthony"
    telefono = "950122470"
    estado_registro = "A"

    insertar_huesped(conexion, codigo, DNI, apellido_materno, apellido_materno,
                    nombre, telefono, estado_registro)


    # Seleccionar registros de la tabla turno_admin
    #seleccionar_turno_admin(conexion)

cerrar_conexion(conexion)