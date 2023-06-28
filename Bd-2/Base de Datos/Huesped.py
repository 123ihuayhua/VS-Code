from db import *

# Función para insertar registros en la tabla huesped
def insertar_huesped(conexion, hue_nom, hue_cod, hue_dni, hue_ape_pat, hue_ape_mat, hue_tel, hue_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO HUESPED (HueCod, HueDNI, HueApePat, HueApeMat, HueNom, HuerTel, HueEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s)"
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
        cursor.execute("SELECT * FROM HUESPED")
        registros = cursor.fetchall()
        print("Registros en la tabla huesped:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla huesped:", error)

# Función para actualizar registros en la tabla huesped
def actualizar_huesped(conexion, hue_cod, lista):
    atr = ["HueCod", "HueDNI", "HueApePat", "HueApeMat", "HueNom", "HuerTel", "HueEstReg"]
    nums = list(lista)

#lista = {4:Rodrigo}
#nums = [4]
#update huesped set HueDNI = s% WHERE %s
#valores(74768623, hue_cod)
#UPDATE HUESPED SET 
    sql = "UPDATE HUESPED SET "
    longitud = len(nums) -1

    for i in range(0, longitud):
        sql = sql + atr[nums[i]] + "= %s,"
    sql = sql + atr[nums[len(nums)-1]] + "= %s WHERE Huecod = %s"

    try:
        cursor = conexion.cursor()
        valores = []
        for i in range(0, len(nums)):
            valores.append(lista[nums[i]])
        valores.append(hue_cod)

        if len(valores) > 1:
            valores = tuple(valores)

        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla huesped.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla huesped:", error)

# Función para eliminar un registro de la tabla huesped
def eliminar_huesped(conexion, hue_cod, tipoDelete):
    try:
        cursor = conexion.cursor()
        if tipoDelete == 1:
            sql = "DELETE FROM HUESPED WHERE HueCod = %s"
            valor = [hue_cod]
        else:
            sql = "UPDATE HUESPED SET HueEstReg = %s WHERE HueCod = %s"
            valor = ('*', hue_cod)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla huesped.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla huesped:", error)