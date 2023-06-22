from db import *

# Función para insertar registros en la tabla renta
def insertar_renta(conexion, ren_cod, ren_hab, ren_fec_ini_año, ren_fec_ini_mes, ren_fec_ini_dia, ren_fec_fin_año, ren_fec_fin_mes, ren_fec_fin_dia, ren_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO renta (RenCod, RenHab, RenFecIniAño, RenFecIniMes, RenFecIniDia, RenFecFinAño, RenFecFinMes, RenFecFinDia,RenEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (ren_cod, ren_hab, ren_fec_ini_año, ren_fec_ini_mes, ren_fec_ini_dia, ren_fec_fin_año,ren_fec_fin_mes, ren_fec_fin_dia, ren_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla renta.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla renta:", error)

# Función para seleccionar todos los registros de la tabla renta
def seleccionar_renta(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM renta")
        registros = cursor.fetchall()
        print("Registros en la tabla renta:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla renta:", error)