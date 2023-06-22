from db import *

# Función para insertar registros en la tabla consumo
def insertar_consumo(conexion, pro_cod, adm_cod, hue_cod, hab_cod, con_fec_año, con_fec_mes, con_fec_dia, pro_pre_uni, con_pro_can, pro_est_reg, con_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO consumo (ConCodPro, ConAdmCod, ConHueCod, ConHabCod, ConFecAño, ConFecMes, ConFecDia, ConPreUni, ConProCan, ConEstPro,ConEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (pro_cod, adm_cod, hue_cod, hab_cod, con_fec_año, con_fec_mes, con_fec_dia, pro_pre_uni, con_pro_can, pro_est_reg, con_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla consumo.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla consumo:", error)

# Función para seleccionar todos los registros de la tabla consumo
def seleccionar_consumo(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM consumo")
        registros = cursor.fetchall()
        print("Registros en la tabla consumo:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla consumo:", error)