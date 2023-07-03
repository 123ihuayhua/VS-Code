from flet import *
import flet as ft
import mysql.connector

#Conexión BD
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    port = 3306,
    password = 'anthony23', #contraseña
    database = 'HOTEL'
)
cursor = mydb.cursor()
def main(page:Page):
    page.scroll = "always"
    page.update()
    #Agregar RENTA
    codtxt = TextField(label="Código")
    rentatxt = TextField(label="Renta")#DNI dnitxt
    yeartxt = TextField(label="Año actual")#apeptxt 
    mestxt = TextField(label="Mes actual")#apemtxt
    diatxt = TextField(label="Dia actual")#nametxt

    year2txt = TextField(label="Año final")#apeptxt 
    mes2txt = TextField(label="Mes final")#apemtxt
    dia2txt = TextField(label="Dia final")#nametxt

    esttxt = Dropdown(
            label="Estado de Registro",
            value="A",
            options=[
                dropdown.Option("A")
                #dropdown.Option("I")
            ]
    )

    #Editar 
    edit_codtxt = TextField(label="Código", disabled=True)
    edit_rentatxt = TextField(label="Renta")
    edit_yeartxt = TextField(label="Año actual") 
    edit_mestxt = TextField(label="Mes actual")
    edit_diatxt = TextField(label="Dia actual")

    edit_year2txt = TextField(label="Año final") 
    edit_mes2txt = TextField(label="Mes final")
    edit_dia2txt = TextField(label="Dia final")

    edit_esttxt = Dropdown(
            label="Estado de Registro",
            disabled=True,
            value="A",
            options=[
                dropdown.Option("A")
                #dropdown.Option("I")
            ]
    )
#---------

    mydt = DataTable(
        columns=[
            DataColumn(Text("Código")),
            DataColumn(Text("Renta")),
            DataColumn(Text("Año actual")),
            DataColumn(Text("Mes actual")),
            DataColumn(Text("Dia actual")),
            DataColumn(Text("Año final")),
            DataColumn(Text("Mes final")),
            DataColumn(Text("Dia final")),
            DataColumn(Text("Estado de Registro")),
            DataColumn(Text("Acciones")),
        ], 
        rows=[]
    )

    #Eliminar elementos
    # def deletebtn(e):
    #     print("El código seleccionado es: ", e.control.data['RenCod'])
    #     try:
    #         sql = "DELETE FROM RENTA WHERE RenCod = %s"
    #         val = (e.control.data['RenCod'],)
    #         cursor.execute(sql,val)
    #         mydb.commit()

    #         print("Renta Eliminada")
    #         mydt.rows.clear()
    #         load_data()
    #         page.snack_bar = SnackBar(
    #             Text("Dato eliminado", size=15),
    #             bgcolor="red",
    #         )
    #         page.snack_bar.open = True
    #         page.update()

    #     except Exception as e:
    #         print(e)
    #         print("Error en el código para eliminar")

    #Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE RENTA SET RenHab = %s, RenFecIniAño = %s, RenFecIniMes = %s, RenFecIniDia = %s, RenFecFinAño = %s, RenFecFinMes = %s, RenFecFinDia = %s WHERE RenCod = %s"
            val = (edit_rentatxt.value, edit_yeartxt.value, edit_mestxt.value, edit_diatxt.value, edit_year2txt.value, edit_mes2txt.value, edit_dia2txt.value, edit_codtxt.value)
            cursor.execute(sql,val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            #Limipiar campos
            edit_rentatxt.value = ""
            edit_yeartxt.value = ""
            edit_mestxt.value = ""
            edit_diatxt.value = ""
            edit_year2txt.value = ""
            edit_mes2txt.value = ""
            edit_dia2txt.value = ""
            edit_esttxt.value = "A", Dropdown(
            label="Estado de Registro",
            value="A",
            options=[
                dropdown.Option("A")
                #dropdown.Option("I")
            ])

            mydt.rows.clear()
            load_data()
            page.snack_bar = SnackBar(
                Text("Dato Actualizado", size=15),
                bgcolor="green",
            )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print("Error al guardar edit!")
    
    #Inactivar registro
    def inactbtn(e):
        try:
            sql = "UPDATE RENTA SET RenEstReg = %s WHERE RenCod = %s"
            val = ('I', edit_codtxt.value)
            cursor.execute(sql, val)
            mydb.commit()
            print("Registro Inactivado")
            dialog.open = False
            page.update()
            
            mydt.rows.clear()
            load_data()
            page.snack_bar = SnackBar(
                Text("Registro Inactivado", size=15),
                bgcolor="gray",
            )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print("Error al inactivar registro!")
    
    
    #Cancelar registro
    def cancelform(e):
        try:
            dialog.open = False
            page.update()
            #Limipiar campos
            #Limipiar campos
            edit_rentatxt.value = ""
            edit_yeartxt.value = ""
            edit_mestxt.value = ""
            edit_diatxt.value = ""
            edit_year2txt.value = ""
            edit_mes2txt.value = ""
            edit_dia2txt.value = ""
            edit_esttxt.value = "A", Dropdown(
            label="Estado de Registro",
            value="A",
            options=[
                dropdown.Option("A")
                #dropdown.Option("I")
            ])

            mydt.rows.clear()
            load_data()
            page.snack_bar = SnackBar(
                Text("Actualización Cancelada", size=15),
                bgcolor="yellow",
            )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print("Error al cancelar edit!")

    #Cuadro de diálogo
    dialog = AlertDialog(
        title=Text("Edit Data"),
        content=Column([
            edit_codtxt,
            edit_rentatxt,
            edit_yeartxt,
            edit_mestxt,
            edit_diatxt,
            edit_year2txt,
            edit_mes2txt,
            edit_dia2txt,
            edit_esttxt ]),
        actions=[
            TextButton("Guardar", on_click=savedata),
            TextButton("Cancelar", on_click=cancelform),
            TextButton("Inactivar", on_click=inactbtn)]
    )
    
    def createbtn(e):
        edit_codtxt.value = e.control.data['RenCod']
        edit_rentatxt.value = e.control.data['RenHab']
        edit_yeartxt.value = e.control.data['RenFecIniAño']
        edit_mestxt.value = e.control.data['RenFecIniMes']
        edit_diatxt.value = e.control.data['RenFecIniDia']
        edit_year2txt.value = e.control.data['RenFecFinAño']
        edit_mes2txt.value = e.control.data['RenFecFinMes']
        edit_dia2txt.value = e.control.data['RenFecFinDia']
        edit_esttxt.value = e.control.data['RenEstReg']

        page.dialog = dialog
        dialog.open = True
        page.update()

    #Activar Registro
    def actbtn(e):
        try:
            sql = "UPDATE RENTA SET RenEstReg = %s WHERE RenCod = %s"
            val = ('A', e.control.data['RenCod'])
            cursor.execute(sql, val)
            mydb.commit()
            print("Registro Activado")
            page.update()
            
            mydt.rows.clear()
            load_data()
            page.snack_bar = SnackBar(
                Text("Registro Activado", size=15),
                bgcolor="skyblue",
            )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print("Error al activar registro!")

    
    #Eliminado lógico
    def dellog(e):
        try:
            sql = "UPDATE RENTA SET RenEstReg = %s WHERE RenCod = %s"
            val = ('*', e.control.data['RenCod'])
            cursor.execute(sql, val)
            mydb.commit()
            print("Eliminado lógico correcto")
            page.update()
            
            mydt.rows.clear()
            load_data()
            page.snack_bar = SnackBar(
                Text("Registro Eliminado Lógicamente", size=15),
                bgcolor="purple",
            )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print("Error al eliminar!")

    def load_data():
        #Obtener datos de la bd
        cursor.execute("SELECT * FROM RENTA")
        result = cursor.fetchall()
        #Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        #Bucle de pusheo 
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['RenCod'])),
                        DataCell(Text(row['RenHab'])),
                        DataCell(Text(row['RenFecIniAño'])),
                        DataCell(Text(row['RenFecIniMes'])),
                        DataCell(Text(row['RenFecIniDia'])),
                        DataCell(Text(row['RenFecFinAño'])),
                        DataCell(Text(row['RenFecFinMes'])),
                        DataCell(Text(row['RenFecFinDia'])),
                        DataCell(Text(row['RenEstReg'])),

                        DataCell(
                            Row(load_icons(row))
                        )
                    ]
                )
            )
            page.update()

    def load_icons(row):
        if (row['RenEstReg'] == 'I'):
            return [IconButton("check_box", icon_color='green',
                                        data=row,
                                        on_click=actbtn)]
        elif (row['RenEstReg'] == '*'):
            return []

        return [
            IconButton("create", icon_color='blue',
                                            data=row,
                                            on_click=createbtn),
            IconButton("stars", icon_color='yellow',
                                            data=row,
                                            on_click=dellog)
        ]

    #Llamar función cuando la aplicación está abierta
    load_data()

    def addtodb(e):
        try:
            sql = "INSERT INTO RENTA (RenCod, RenHab, RenFecIniAño, RenFecIniMes, RenFecIniDia, RenFecFinAño, RenFecFinMes, RenFecFinDia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (codtxt.value, rentatxt.value, yeartxt.value, mestxt.value, diatxt.value, year2txt.value, mes2txt.value, dia2txt.value)
            cursor.execute(sql, val)
            mydb.commit()
            print(cursor.rowcount, "You record insert!")

            #Limpiar columnas
            mydt.rows.clear()
            load_data()

            page.snack_bar = SnackBar(
                Text("Dato agregado", size=15),
                bgcolor="green",
            )
            page.snack_bar.open = True
            page.update()
        
        except Exception as e:
            print(e)
            print("Error en el código")

        #Limpiar el texinput
        codtxt.value = ""
        rentatxt.value = ""
        yeartxt.value = ""
        mestxt.value = ""
        diatxt.value = ""
        year2txt.value = ""
        mes2txt.value = ""
        dia2txt.value = ""
        esttxt.value = "A", Dropdown(
            label="Estado de Registro",
            value="A",
            options=[
                dropdown.Option("A")
                #dropdown.Option("I")
            ])
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            codtxt.value = ""
            rentatxt.value = ""
            yeartxt.value = ""
            mestxt.value = ""
            diatxt.value = ""
            year2txt.value = ""
            mes2txt.value = ""
            dia2txt.value = ""
            esttxt.value = "A" , Dropdown(
            label="Estado de Registro",
            value="A",
            options=[
                dropdown.Option("A")
                #dropdown.Option("I")
            ])
            
            page.update()
            mydt.rows.clear()
            load_data()
            page.snack_bar = SnackBar(
                    Text("Registro Cancelado", size=15),
                    bgcolor="yellow",
                )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print("Error en el código")
    
    page.add(
        Column([
            codtxt, rentatxt, yeartxt, mestxt, diatxt, year2txt, mes2txt, dia2txt, esttxt,
            Row([
                ElevatedButton("AGREGAR", on_click=addtodb),
                ElevatedButton("CANCELAR", on_click=cancelIn),
            ]),
            mydt,
            ], 
        ),
    )
    
flet.app(target=main)