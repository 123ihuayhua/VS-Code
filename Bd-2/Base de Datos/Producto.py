from db import *

# Función para insertar registros en la tabla producto
def insertar_producto(conexion, pro_cod, pro_pre_uni, pro_nom, pro_sto, pro_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO producto (ProCod, ProPreUni, ProNom, ProSto, ProEstReg) VALUES (%s, %s, %s, %s, %s)"
        valores = (pro_cod, pro_pre_uni, pro_nom, pro_sto, pro_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla producto.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla producto:", error)

# Función para seleccionar todos los registros de la tabla producto
def seleccionar_producto(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM producto")
        registros = cursor.fetchall()
        print("Registros en la tabla producto:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla producto:", error)

# Función para actualizar registros en la tabla producto
def actualizar_producto(conexion, pro_cod, pro_pre_uni, pro_nom, pro_sto, pro_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE producto SET ProPreUni = %s, ProNom = %s, ProSto = %s, ProEstReg = %s WHERE ProCod = %s"
        valores = (pro_cod, pro_pre_uni, pro_nom, pro_sto, pro_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla producto.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla producto:", error)

# Función para eliminar un registro de la tabla producto
def eliminar_producto(conexion, pro_cod):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM producto WHERE ProCod = %s"
        valor = (pro_cod)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla producto.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla producto:", error)