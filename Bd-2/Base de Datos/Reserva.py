from db import *

# Función para insertar registros en la tabla reserva
def insertar_reserva(conexion, hue_cod, adm_cod, hab_cod, fec_ent_año, fec_ent_mes, fec_ent_dia, fec_sal_año, fec_sal_mes, fec_sal_dia, res_est_reg, res_est_reg2):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO reserva (ResHueCod, ResAdmCod, ResHabCod, ResFecEntAño, ResFecEntMes, ResFecEntDia, ResFecSalAño, ResFecSalMes, ResFecSalDia, ResEstRes, ResEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (hue_cod, adm_cod, hab_cod, fec_ent_año, fec_ent_mes, fec_ent_dia, fec_sal_año, fec_sal_mes, fec_sal_dia, res_est_reg, res_est_reg2)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla reserva.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla reserva:", error)

# Función para seleccionar todos los registros de la tabla reserva
def seleccionar_reserva(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM reserva")
        registros = cursor.fetchall()
        print("Registros en la tabla reserva:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla reserva:", error)