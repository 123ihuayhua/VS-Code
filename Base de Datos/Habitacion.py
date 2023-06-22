from db import *

# Función para insertar registros en la tabla habitacion
def insertar_habitacion(conexion, hab_cod, hab_cat_cod, hab_pis, hab_num, hab_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO habitacion (HabCod, HabCatCod, HabPis, HabNumHab, HabEstReg) VALUES (%s, %s, %s, %s, %s)"
        valores = (hab_cod, hab_cat_cod, hab_pis, hab_num, hab_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla habitacion.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla habitacion:", error)

# Función para seleccionar todos los registros de la tabla habitacion
def seleccionar_habitacion(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM habitacion")
        registros = cursor.fetchall()
        print("Registros en la tabla habitacion:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla habitacion:", error)