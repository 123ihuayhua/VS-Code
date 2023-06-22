from db import *

# Función para insertar registros en la tabla habitacion_categoria
def insertar_habitacion_categoria(conexion, hab_cat_cod, hab_cat_ren, hab_cat_des, hab_cat_img, hab_cat_cap, hab_cat_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO habitacion_categoria (HabCatCod, HabCatRen, HabCatDes, HabCatIma, HabCatCap, HabCatEstReg) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (hab_cat_cod, hab_cat_ren, hab_cat_des, hab_cat_img, hab_cat_cap, hab_cat_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla habitacion_categoria.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla habitacion_categoria:", error)

# Función para seleccionar todos los registros de la tabla habitacion_categoria
def seleccionar_habitacion_categoria(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM habitacion_categoria")
        registros = cursor.fetchall()
        print("Registros en la tabla habitacion_categoria:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla habitacion_categoria:", error)