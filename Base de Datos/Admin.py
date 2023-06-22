from db import *

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

# Función para actualizar registros en la tabla administrador
def actualizar_administrador(conexion, codigo, tur_cod, dni, ape_pat, ape_mat, adm_nom, est_reg):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE administrador SET AdmTur = %s, AdmDNI = %s, AdmApePat = %s, AdmApeMat = %s, AdmNom = %s, AdmEstReg = %s WHERE AdmCod = %s"
        valores = (codigo, tur_cod, dni, ape_pat, ape_mat, adm_nom, est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla administrador.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla administrador:", error)

# Función para eliminar un registro de la tabla administrador
def eliminar_cliente(conexion, codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM administrador WHERE AdmCod = %s"
        valor = (codigo)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla administrador.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla administrador:", error)