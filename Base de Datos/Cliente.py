from db import *

# Función para insertar registros en la tabla cliente
def insertar_cliente(conexion, hue_cod, cli_ruc, cli_emp_nom, cli_emp_raz_soc, cli_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO cliente (CliHueCod, CliRUC, CliEmpNom, CliRazSoc, CliEstReg) VALUES (%s, %s, %s, %s, %s)"
        valores = (hue_cod, cli_ruc, cli_emp_nom, cli_emp_raz_soc, cli_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla cliente.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla cliente:", error)

# Función para seleccionar todos los registros de la tabla cliente
def seleccionar_cliente(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente")
        registros = cursor.fetchall()
        print("Registros en la tabla cliente:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla cliente:", error)

# Función para actualizar registros en la tabla cliente
def actualizar_cliente(conexion, hue_cod, cli_ruc, cli_emp_nom, cli_emp_raz_soc, cli_est_reg):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE cliente SET CliRUC = %s, CliEmpNom = %s, CliEmpNom = %s, CliRazSoc = %s, CliEstReg = %s WHERE CliHueCod = %s"
        valores = (hue_cod, cli_ruc, cli_emp_nom, cli_emp_raz_soc, cli_est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla cliente.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla cliente:", error)

# Función para eliminar un registro de la tabla cliente
def eliminar_cliente(conexion, hue_cod):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM cliente WHERE CliHueCod = %s"
        valor = (hue_cod)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla cliente.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla cliente:", error)