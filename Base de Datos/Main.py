from db import *
from Huesped import *

def ingresarHuesped():
    #Datos Huesped
    #codigo = int(input("CODIGO: "))
    DNI = input("DNI: ")
    apellido_paterno = input("APELLIDO PATERNO: ")
    apellido_materno = input("APELLIDO MATERNO: ")
    nombre = input("NOMBRE: ")
    telefono = input("TELEFONO: ")
    estado_registro = input("ESTADO DE REGISTRO")

def menu():
    cadena = "Opciones para Huesped:\n[1] CREAR\n[2] SELECCIONAR\n[3] ACTUALIZAR\n[4] ELIMINAR\nOPCION: "
    opcion = input (cadena)
    opcion = int(opcion)

    if opcion == 1:
        global nombre, telefono, estado_registro
        insertar_huesped(conexion, nombre, codigo, DNI, apellido_paterno, apellido_materno, telefono, estado_registro)
        print("\n", "Huesped creado exitosamente")
    elif opcion == 2:
        seleccionar_huesped(conexion)
    elif opcion == 3:
        print("Seleccione los atributos a actualizar\n")
        longitud = len(atributos)
        for i in range(1, longitud):
            print("[", i, "] ", atributos[i])
        opcion2 = 1
        lista = {}
        while (opcion2 == 1):
            num = int(input("Campo a cambiar: "))
            valor = input("Nuevo valor: ")
            lista[num] = valor

            opcion2 = int(input("Seguir agregando?\n[0] NO\t[1] SI\nOPCION: "))

        actualizar_huesped(conexion, codigo, lista)
    elif opcion == 4:
        value = int(input("[0] LOGICO\n[1] FISICO\nOPCION: "))
        eliminar_huesped(conexion, codigo, value)

# Establecer la conexión a la base de datos
conexion = establecer_conexion()

#Datos Huesped
codigo = int(input("CODIGO: "))
DNI = input("DNI: ")
apellido_paterno = input("APELLIDO PATERNO: ")
apellido_materno = input("APELLIDO MATERNO: ")
nombre = input("NOMBRE: ")
telefono = input("TELEFONO: ")
estado_registro = input("ESTADO DE REGISTRO")

atributos = ["HueCod", "HueDNI", "HueApePat", "HueApeMat", "HueNom", "HuerTel", "HueEstReg"]

option = 1
while (option == 1):
    if conexion is not None:
        menu()
    option = int(input("¿DESEA SEGUIR?\n[0] NO\t[1] SI\nOPCION: "))

cerrar_conexion(conexion)