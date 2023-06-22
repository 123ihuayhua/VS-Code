from db import *
from datetime import time 

# Función para insertar registros en la tabla turno_admin
def insertar_turno_Admin(conexion, codigo, hora_entrada, hora_salida, est_reg):
    try:
        cursor = conexion.cursor()
        # Convertir las cadenas de tiempo a objetos time
        hora_entrada = time.fromisoformat(hora_entrada)
        hora_salida = time.fromisoformat(hora_salida)

        sql = "INSERT INTO turno_admin ( TurAdmCod,  TurAdmHorEnt,  TurHorSal, TurEstReg) VALUES (%s, %s, %s, %s)"
        valores = (codigo, hora_entrada, hora_salida, est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla turno_admin.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla turno_admin:", error)

# Función para seleccionar todos los registros de la tabla turno_admin
def seleccionar_turno_admin(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM turno_admin")
        registros = cursor.fetchall()
        print("Registros en la tabla turno_admin:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla turno_admin:", error)

# Función para insertar registros en la tabla administrador
def insertar_administrador(conexion, codigo, tur_cod, dni, ape_pat, ape_mat, adm_nom, est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO administrador (AdmCod, AdmTur, AdmDNI, AdmApePat, AdmApeMat, AdmNom, AdmEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (codigo, tur_cod, dni, ape_pat, ape_mat, adm_nom, est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla administrador.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla administrador:", error)

# Función para seleccionar todos los registros de la tabla administrador
def seleccionar_administrador(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM administrador")
        registros = cursor.fetchall()
        print("Registros en la tabla administrador:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla administrador:", error)
