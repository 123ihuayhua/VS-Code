from db import *
from datetime import time 

# Función para insertar registros en la tabla turno_admin
def insertar_turno_Admin(conexion, codigo, hora_entrada, hora_salida, est_reg):
    try:
        cursor = conexion.cursor()
        # Convertir las cadenas de tiempo a objetos time
        hora_entrada = time.fromisoformat(hora_entrada)
        hora_salida = time.fromisoformat(hora_salida)

        sql = "INSERT INTO turno_admin ( TurAdmCod,  TurAdmHorEnt,  TurHorSal, TurEstReg) VALUES (%s, %s, %s, %s)"
        valores = (codigo, hora_entrada, hora_salida, est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla turno_admin.")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla turno_admin:", error)

# Función para seleccionar todos los registros de la tabla turno_admin
def seleccionar_turno_admin(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM turno_admin")
        registros = cursor.fetchall()
        print("Registros en la tabla turno_admin:")
        for registro in registros:
            print(registro)
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla turno_admin:", error)

# Función para actualizar registros en la tabla turno_admin
def actualizar_turno_admin(conexion, codigo, hora_entrada, hora_salida, est_reg):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE turno_admin SET TurAdmHorEnt = %s, TurHorSal = %s, TurEstReg = %s WHERE TurAdmCod = %s"
        valores = (codigo, hora_entrada, hora_salida, est_reg)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla turno_admin.")
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla turno_admin:", error)

# Función para eliminar un registro de la tabla turno_admin
def eliminar_cliente(conexion, codigo):
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM turno_admin WHERE TurAdmCod = %s"
        valor = (codigo,)
        cursor.execute(sql, valor)
        conexion.commit()
        print("Registro eliminado correctamente de la tabla turno_admin.")
    except mysql.connector.Error as error:
        print("Error al eliminar registro de la tabla turno_admin:", error)