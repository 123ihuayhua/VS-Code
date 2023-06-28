from db import *

# Función para insertar registros en la tabla boleta_cabecera
def insertar_boleta_cabecera(conexion, bol_cod, hot_cod, cli_cod, bol_fec_año, bol_fec_mes, bol_fec_dia, est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO boleta_cabecera (BolCabCod, BolCabHotCod, BolCabCliCod, BolCabFecAño, BolCabFecMes, BolCabFecDia, BolCabEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (bol_cod, hot_cod, cli_cod, bol_fec_año, bol_fec_mes, bol_fec_dia, est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla boleta_cabecera.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla boleta_cabecera:", error)

# Función para seleccionar todos los registros de la tabla boleta_cabecera
def seleccionar_boleta_cabecera(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM boleta_cabecera")
        registros = cursor.fetchall()
        print("Registros en la tabla boleta_cabecera:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla boleta_cabecera:", error)


