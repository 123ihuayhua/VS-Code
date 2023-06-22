from db import *

# Función para insertar registros en la tabla huesped
def insertar_huesped(conexion, hue_cod, hue_dni, hue_ape_pat, hue_ape_mat, hue_nom, hue_tel, hue_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO huesped (HueCod, HueDNI, HueApePat, HueApeMat, HueNom, HuerTel, HueEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (hue_cod, hue_dni, hue_ape_pat, hue_ape_mat, hue_nom, hue_tel, hue_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla huesped.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla huesped:", error)

# Función para seleccionar todos los registros de la tabla huesped
def seleccionar_huesped(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM huesped")
        registros = cursor.fetchall()
        print("Registros en la tabla huesped:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla huesped:", error)

# Función para actualizar registros en la tabla huesped
def actualizar_huesped(conexion, hue_cod, hue_dni, hue_ape_pat, hue_ape_mat, hue_nom, hue_tel, hue_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE huesped SET HueDNI = %s, HueApePat = %s, HueApeMat = %s, HueNom = %s, HuerTel = %s, HueEstReg = %s, WHERE HueCod = %s"
        valores = (hue_cod, hue_dni, hue_ape_pat, hue_ape_mat, hue_nom, hue_tel, hue_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla huesped.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla huesped:", error)

# Función para eliminar un registro de la tabla huesped
def eliminar_cliente(conexion, hue_cod):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM huesped WHERE HueCod = %s"
        valor = (hue_cod)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla huesped.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla huesped:", error)