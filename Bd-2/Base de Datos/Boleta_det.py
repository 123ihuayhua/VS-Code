from db import *

# Función para insertar registros en la tabla boleta_detalle
def insertar_boleta_detalle(conexion, bol_cod, hue_cod, adm_cod, hab_cod, bol_fec_ent_año, bol_fec_ent_mes, bol_fec_ent_dia, bol_fec_sal_año, bol_fec_sal_mes, bol_fec_sal_dia, hab_cat_cod, hab_ren, total, est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO boleta_detalle (BolDetCod, BolDetHueCod, BolDetAdmCod,  BolDetHabCod,  BolDetFecEntAño,  BolDetFecEntMes,  BolDetFecEntDia,  BolDetFecSalAño, BolDetFecSalMes, BolDetFecSalDia, BolDetCatHabDes,  BolDetRen,  BolDetTot, BolDetEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (bol_cod, hue_cod, adm_cod, hab_cod, bol_fec_ent_año, bol_fec_ent_mes, bol_fec_ent_dia, bol_fec_sal_año, bol_fec_sal_mes, bol_fec_sal_dia, hab_cat_cod, hab_ren, total, est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla boleta_detalle.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla boleta_detalle:", error)

# Función para seleccionar todos los registros de la tabla boleta_detalle
def seleccionar_boleta_detalle(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM boleta_detalle")
        registros = cursor.fetchall()
        print("Registros en la tabla boleta_detalle:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla boleta_detalle:", error)