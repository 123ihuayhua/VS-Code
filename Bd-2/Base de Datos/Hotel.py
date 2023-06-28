from db import *

# Función para insertar registros en la tabla hotel
def insertar_hotel(conexion, hot_cod, hot_ruc, hot_nom, hot_ape_pat_due, hot_ape_mat_due, hot_nom_due, hot_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO hotel (HotCod, HotRUC, HotNom, HotApePatDue, HotApeMatDue, HotNomDue, HotEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (hot_cod, hot_ruc, hot_nom, hot_ape_pat_due, hot_ape_mat_due, hot_nom_due, hot_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla hotel.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla hotel:", error)

# Función para seleccionar todos los registros de la tabla hotel
def seleccionar_hotel(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM hotel")
        registros = cursor.fetchall()
        print("Registros en la tabla habitacion:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla habitacion:", error)