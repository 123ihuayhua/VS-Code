import time
from flet import *
import flet as ft
import mysql.connector
from flet import *

# Conexión BD
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    port=3306,
    password='lm10kayca',  # contraseña
    database='HOTEL'
)
cursor = mydb.cursor()

# Estructura


def main(page: Page):
    page.scroll = "always"
    page.update()
    # Agregar RENTA
    codtxt = TextField(label="Código")
    rentatxt = TextField(label="Renta")  # DNI dnitxt
    yeartxt = TextField(label="Año actual")  # apeptxt
    mestxt = TextField(label="Mes actual")  # apemtxt
    diatxt = TextField(label="Dia actual")  # nametxt

    year2txt = TextField(label="Año final")  # apeptxt
    mes2txt = TextField(label="Mes final")  # apemtxt
    dia2txt = TextField(label="Dia final")  # nametxt

    # esttxt = Dropdown(
    #         label="Estado de Registro",
    #         value="A",
    #         options=[
    #             dropdown.Option("A"),
    #         ]
    # )

    # Editar
    edit_codtxt = TextField(label="Código", disabled=True)
    edit_rentatxt = TextField(label="Renta")  # DNI dnitxt
    edit_yeartxt = TextField(label="Año actual")  # apeptxt
    edit_mestxt = TextField(label="Mes actual")  # apemtxt
    edit_diatxt = TextField(label="Dia actual")  # nametxt

    edit_year2txt = TextField(label="Año final")  # apeptxt
    edit_mes2txt = TextField(label="Mes final")  # apemtxt
    edit_dia2txt = TextField(label="Dia final")  # nametxt

    edit_esttxt = Dropdown(
            label="Estado de Registro",
            disabled=True,
            value="A",
            options=[
                dropdown.Option("A"),
            ]
    )
# ---------

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

    # Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE RENTA SET RenHab = %s, RenFecIniAño = %s, RenFecIniMes = %s, RenFecIniDia = %s, RenFecFinAño = %s, RenFecFinMes = %s, RenFecFinDia = %s, RenEstReg = %s WHERE RenCod = %s"
            val = (edit_rentatxt.value, edit_yeartxt.value, edit_mestxt.value, edit_diatxt.value,
                   edit_year2txt.value, edit_mes2txt.value, edit_dia2txt.value, edit_esttxt.value, edit_codtxt.value)
            cursor.execute(sql, val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            # Limipiar campos
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
                dropdown.Option("A"),
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

    # Inactivar registro
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

    # Cancelar registro
    def cancelform(e):
        try:
            dialog.open = False
            page.update()
            # Limipiar campos
            # Limipiar campos
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
                dropdown.Option("A"),
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

    # Cuadro de diálogo
    dialog = AlertDialog(
        title=Text("Editar Registro"),
        content=Column([
            edit_codtxt,
            edit_rentatxt,
            edit_yeartxt,
            edit_mestxt,
            edit_diatxt,
            edit_year2txt,
            edit_mes2txt,
            edit_dia2txt,
            edit_esttxt]),
        actions=[
            TextButton("Guardar", on_click=savedata),
            TextButton("Cancelar", on_click=cancelform),
            TextButton("Inactivar", on_click=inactbtn)]
    )

    #Editar
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

    # Activar Registro
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

    # Eliminado lógico
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

    # Cargar datos
    def load_data():
        # Obtener datos de la bd
        cursor.execute("SELECT * FROM RENTA")
        result = cursor.fetchall()
        # Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        # Bucle de pusheo
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
                        ),
                    ],
                    selected=True,
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                )
            )
            page.update()

    #Buscar datos
    # #Obtener cod de la bd 
    # def inputsearch(e):
    #     # Obtener datos de la bd
    #     cursor.execute("SELECT * FROM RENTA WHERE RenCod = %s")
    #     result = cursor.fetchall()
    #     # Push al diccionario
    #     columns = [column[0] for column in cursor.description]
    #     rows = [dict(zip(columns, row)) for row in result]

    #     # Bucle de pusheo
    #     for row in rows:
    #         mydt.rows.append(
    #             DataRow(
    #                 cells=[
    #                     DataCell(Text(row['RenCod'])),
    #                     DataCell(Text(row['RenHab'])),
    #                     DataCell(Text(row['RenFecIniAño'])),
    #                     DataCell(Text(row['RenFecIniMes'])),
    #                     DataCell(Text(row['RenFecIniDia'])),
    #                     DataCell(Text(row['RenFecFinAño'])),
    #                     DataCell(Text(row['RenFecFinMes'])),
    #                     DataCell(Text(row['RenFecFinDia'])),
    #                     DataCell(Text(row['RenEstReg'])),

    #                     DataCell(
    #                         Row(load_icons(row))
    #                     )
    #                 ]
    #             )
    #         )
    #     page.update()

    # nameinput = TextField(label="Search Código", on_change=inputsearch)
    # # Si no hay dato
    # datanotfound = Text("Dato no encontrado...", weight="bold", size=20,)
    # datanotfound.visible = False

    def load_icons(row):
            if (row['RenEstReg'] == 'I' or row['RenEstReg'] == '*'):
                return [IconButton("check_box", icon_color='green',
                                            data=row,
                                            on_click=actbtn)]

            return [
                IconButton("create", icon_color='blue',
                                                data=row,
                                                on_click=createbtn),
                IconButton("stars", icon_color='yellow',
                                                data=row,
                                                on_click=dellog)
            ]


    #Llamar función cuando la aplicación está abierta
    
    #Agregar datos boton
    def addtodb(e):
        try:
            sql = "INSERT INTO RENTA (RenCod, RenHab, RenFecIniAño, RenFecIniMes, RenFecIniDia, RenFecFinAño, RenFecFinMes, RenFecFinDia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (codtxt.value, rentatxt.value, yeartxt.value, mestxt.value, diatxt.value, year2txt.value, mes2txt.value, dia2txt.value, )
            cursor.execute(sql, val)
            mydb.commit()
            print(cursor.rowcount, "You record insert!")

            #Limpiar columnas
            mydt.rows.clear()
            load_data()
            dialog2.open = False
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
        # esttxt.value = "A", Dropdown(
        #     label="Estado de Registro",
        #     value="A",
        #     options=[
        #         dropdown.Option("A"),
        #     ])
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            dialog2.open = False
            codtxt.value = ""
            rentatxt.value = ""
            yeartxt.value = ""
            mestxt.value = ""
            diatxt.value = ""
            year2txt.value = ""
            mes2txt.value = ""
            dia2txt.value = ""
            # esttxt.value = "A" , Dropdown(
            # label="Estado de Registro",
            # value="A",
            # options=[
            #     dropdown.Option("A"),
            # ])
            
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
    
    # Cuadro de diálogo Ingresar datos
    dialog2 = AlertDialog(
        StadiumBorder,
        title = Text("Ingresar Datos"),
        content = Column([
            codtxt,
            rentatxt,
            yeartxt,
            mestxt,
            diatxt,
            year2txt,
            mes2txt,
            dia2txt,
            # esttxt
        ]),
        actions = [
            TextButton("AGREGAR", on_click=addtodb),
            TextButton("CANCELAR", on_click=cancelIn),
        ]
    )

    #Boton redireccionamiento
    def AddBtn(e):
        codtxt.value = ""
        rentatxt.value = ""
        yeartxt.value = ""
        mestxt.value = ""
        diatxt.value = ""
        year2txt.value = ""
        mes2txt.value = ""
        dia2txt.value = ""
        # esttxt.value = ""
        page.dialog = dialog2
        dialog2.open = True
        page.update()
    
    #Color thema defecto 
    page.theme_mode = "light"
    page.splash = ProgressBar(visible=False)

    #Funcion cambio de tema
    def changetheme(e):
        page.splash.visible = True
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

        #Tiempo espera
        time.sleep(0.5)
        toggledarklight.selected = not toggledarklight.selected
        page.splash.visible = False
        page.update()

    #Cambio de dark/light
    toggledarklight = IconButton(
        on_click = changetheme,
        icon = "dark_mode",
        selected_icon = "light_mode",
        style = ButtonStyle(
            color = {"":colors.BLACK, "selected":colors.WHITE}
        )
    )
    #Salir
    def exit_app(e):
        page.window_destroy()
        
    load_data()
    #Main
    page.title = "Rentas"
    page.window_maximized = True
    page.add(
        AppBar(
            title = Text("TABLA RENTAS", size = 30),
            bgcolor = colors.TEAL,
            actions = [toggledarklight]
        ),
        ft.Column([
            ft.Row([
                Container(
                    ft.FloatingActionButton(icon=ft.icons.CREATE, text="AGREGAR", on_click=AddBtn),
                ),
                Container(
                    ft.FloatingActionButton(text = "SALIR", icon=ft.icons.CLOSE, on_click=exit_app, bgcolor=ft.colors.RED),
                ),
            ]),
        ]),
        # nameinput,
        ft.Divider(),
        Container(mydt, alignment=ft.alignment.center),
    )
    
ft.app(target=main)