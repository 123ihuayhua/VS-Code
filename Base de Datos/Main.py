from db import *
from Huesped import *

# Establecer la conexión a la base de datos
conexion = establecer_conexion()

#Datos Huesped
codigo = 234510
DNI = "74768625"
apellido_paterno = "Moroccoire"
apellido_materno = "Pacompia"
nombre = "Anthony"
telefono = "950122470"
estado_registro = "A"

def menu():
    cadena = "Opciones para Huesped:\n[1] CREAR\n[2] SELECCIONAR\n[3] ACTUALIZAR\n[4] ELIMINAR\nOPCION: "
    opcion = input (cadena)
    opcion = int(opcion)

    if opcion == 1:
        global nombre, telefono, estado_registro
        insertar_huesped(conexion, nombre, codigo, DNI, apellido_paterno, apellido_materno, telefono, estado_registro)
    elif opcion == 2:
        seleccionar_huesped(conexion)
    elif opcion == 3:
        nombre = "Marcos"
        telefono = "950122457"
        estado_registro = "I"
        actualizar_huesped(conexion, codigo, nombre, telefono, estado_registro)
    elif opcion == 4:
        tipoDelete = False
        eliminar_huesped(conexion, codigo, tipoDelete)

if conexion is not None:
    menu()

cerrar_conexion(conexion)