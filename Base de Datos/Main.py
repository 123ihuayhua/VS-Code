from db import *
from V1M_Huesped import *

def ingresarHuesped():
    #Datos Huesped
    codigo = int(input("CODIGO: "))
    DNI = input("DNI: ")
    apellido_paterno = input("APELLIDO PATERNO: ")
    apellido_materno = input("APELLIDO MATERNO: ")
    nombre = input("NOMBRE: ")
    telefono = input("TELEFONO: ")
    estado_registro = input("ESTADO DE REGISTRO: ")
    return Huesped(codigo, DNI, apellido_paterno, apellido_materno, nombre, telefono, estado_registro)

def operacion(opcion, huesped, conexion):
    if huesped == "":
        return "Debe crear un huesped"

    if opcion == 1:
        huesped.insertar_huesped(conexion)
        print("\n", "Huesped creado exitosamente")
    elif opcion == 2:
        huesped.seleccionar_huesped(conexion)
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

        huesped.actualizar_huesped(conexion, lista)
    elif opcion == 4:
        value = int(input("[0] LOGICO\n[1] FISICO\nOPCION: "))
        huesped.eliminar_huesped(conexion, value)
    return "Hecho\n"

def menu():
    cadena = "Opciones para Huesped:\n[1] CREAR\n[2] SELECCIONAR\n[3] ACTUALIZAR\n[4] ELIMINAR\nOPCION: "
    opcion = input (cadena)
    opcion = int(opcion)
    if (opcion < 1 or opcion > 4):
        return -1
    return opcion
# Establecer la conexión a la base de datos
conexion = establecer_conexion()

atributos = ["HueCod", "HueDNI", "HueApePat", "HueApeMat", "HueNom", "HuerTel", "HueEstReg"]

option = 1
huesped = ""
while (option == 1):
    if (conexion is not None) :
        resultado = menu()
        if (resultado == -1) :
            print("Opcion no encontrada")
        if (resultado == 1) :
            huesped = ingresarHuesped()
        print(operacion(resultado, huesped, conexion))
        
    option = int(input("¿DESEA SEGUIR?\n[0] NO\t[1] SI\nOPCION: "))
    if (option > 1 or option < 0):
        option = 1;
        print("Opcion equivocada")

cerrar_conexion(conexion)