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
    # Agregar RESERVA
    huecod = TextField(label="Código Huesped")
    admcod = TextField(label="Código Administrador")  
    habcod = TextField(label="Código Habitación")  
    fecentaño = TextField(label="Fecha Entrada Año")  
    fecentmes = TextField(label="Fecha Entrada Mes")  
    fecentdia = TextField(label="Fecha Entrada Dia")  
    fecsalaño = TextField(label="Fecha Salida Año")  
    fecsalmes = TextField(label="Fecha Salida Mes")  
    fecsaldia = TextField(label="Fecha Salida Dia")  
    resest = TextField(label="Estado Reserva")  

    # Editar
    edit_huecod = TextField(label="Código Huesped", disabled=True)
    edit_admcod = TextField(label="Código Administrador")  
    edit_habcod = TextField(label="Código Habitación")  
    edit_fecentaño = TextField(label="Fecha Entrada Año")  
    edit_fecentmes = TextField(label="Fecha Entrada Mes")  
    edit_fecentdia = TextField(label="Fecha Entrada Dia")  
    edit_fecsalaño = TextField(label="Fecha Salida Año")  
    edit_fecsalmes = TextField(label="Fecha Salida Mes")  
    edit_fecsaldia = TextField(label="Fecha Salida Dia")  
    edit_resest = TextField(label="Estado Reserva") 
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
            DataColumn(Text("Huesped")),
            DataColumn(Text("Administrador")),
            DataColumn(Text("Habitación")),
            DataColumn(Text("Año E.")),
            DataColumn(Text("Mes E.")),
            DataColumn(Text("Dia E.")),
            DataColumn(Text("Año S.")),
            DataColumn(Text("Mes S.")),
            DataColumn(Text("Dia S.")),
            DataColumn(Text("Estado Reserva")),
            DataColumn(Text("Estado de Registro")),
            DataColumn(Text("Acciones")),
        ],
        rows=[]
    )

    # Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE RESERVA SET ResAdmCod = %s, ResHabCod = %s, ResFecEntAño = %s, ResFecEntMes = %s, ResFecEntDia = %s, ResFecSalAño = %s, ResFecSalMes = %s, ResFecSalDia = %s, ResEstRes = %s WHERE ResHueCod = %s"
            val = (edit_admcod.value, edit_habcod.value, edit_fecentaño.value, edit_fecentmes.value, edit_fecentdia.value, edit_fecsalaño.value, edit_fecsalmes.value, edit_fecsaldia.value, edit_resest.value, edit_huecod.value)
            cursor.execute(sql, val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            # Limipiar campos
            edit_admcod.value = ""
            edit_habcod.value = ""
            edit_fecentaño.value = ""
            edit_fecentmes.value = ""
            edit_fecentdia.value = ""
            edit_fecsalaño.value = ""
            edit_fecsalmes.value = ""
            edit_fecsaldia.value = ""
            edit_resest.value = ""
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
            sql = "UPDATE RESERVA SET ResEstReg = %s WHERE ResHueCod = %s"
            val = ('I', edit_huecod.value)
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
            # Limpiar campos
            edit_admcod.value = ""
            edit_habcod.value = ""
            edit_fecentaño.value = ""
            edit_fecentmes.value = ""
            edit_fecentdia.value = ""
            edit_fecsalaño.value = ""
            edit_fecsalmes.value = ""
            edit_fecsaldia.value = ""
            edit_resest.value = ""
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
            edit_admcod,
            edit_habcod,
            edit_fecentaño,
            edit_fecentmes,
            edit_fecentdia,
            edit_fecsalaño,
            edit_fecsalmes,
            edit_fecsaldia,
            edit_resest,
            edit_esttxt],
            scroll=ft.ScrollMode.ALWAYS),
        actions=[
            TextButton("Guardar", on_click=savedata),
            TextButton("Cancelar", on_click=cancelform),
            TextButton("Inactivar", on_click=inactbtn)]
    )

    #Editar
    def createbtn(e):
        edit_huecod.value = e.control.data['ResHueCod']
        edit_admcod.value = e.control.data['ResAdmCod']
        edit_habcod.value = e.control.data['ResHabCod']
        edit_fecentaño.value = e.control.data['ResFecEntAño']
        edit_fecentmes.value = e.control.data['ResFecEntMes']
        edit_fecentdia.value = e.control.data['ResFecEntDia']
        edit_fecsalaño.value = e.control.data['ResFecSalAño']
        edit_fecsalmes.value = e.control.data['ResFecSalMes']
        edit_fecsaldia.value = e.control.data['ResFecSalDia']
        edit_resest.value = e.control.data['ResEstRes']
        edit_esttxt.value = e.control.data['ResEstReg']

        page.dialog = dialog
        dialog.open = True
        page.update()

    # Activar Registro
    def actbtn(e):
        try:
            sql = "UPDATE RESERVA SET ResEstReg = %s WHERE ResHueCod = %s"
            val = ('A', e.control.data['ResHueCod'])
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
            sql = "UPDATE RESERVA SET ResEstReg = %s WHERE ResHueCod = %s"
            val = ('*', e.control.data['ResHueCod'])
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
        cursor.execute("SELECT * FROM RESERVA")
        result = cursor.fetchall()
        # Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        # Bucle de pusheo
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['ResHueCod'])),
                        DataCell(Text(row['ResAdmCod'])),
                        DataCell(Text(row['ResHabCod'])),
                        DataCell(Text(row['ResFecEntAño'])),
                        DataCell(Text(row['ResFecEntMes'])),
                        DataCell(Text(row['ResFecEntDia'])),
                        DataCell(Text(row['ResFecSalAño'])),
                        DataCell(Text(row['ResFecSalMes'])),
                        DataCell(Text(row['ResFecSalDia'])),
                        DataCell(Text(row['ResEstRes'])),
                        DataCell(Text(row['ResEstReg'])),
                        DataCell(
                            Row(load_icons(row))
                        ),
                    ],
                    selected=True,
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                )
            )
            page.update()

    #Iconos
    def load_icons(row):
            if (row['ResEstReg'] == 'I' or row['ResEstReg'] == '*'):
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
    load_data()
    #Agregar datos boton
    def addtodb(e):
        try:
            sql = "INSERT INTO RESERVA (ResHueCod, ResAdmCod, ResHabCod, ResFecEntAño, ResFecEntMes, ResFecEntDia, ResFecSalAño, ResFecSalMes, ResFecSalDia, ResEstRes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (huecod.value, admcod.value, habcod.value, fecentaño.value, fecentmes.value, fecentdia.value, fecsalaño.value, fecsalmes.value, fecsaldia.value, resest.value, )
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
        huecod.value = ""
        admcod.value = ""
        habcod.value = ""
        fecentaño.value = ""
        fecentmes.value = ""
        fecentdia.value = ""
        fecsalaño.value = ""
        fecsalmes.value = ""
        fecsaldia.value = ""
        resest.value = ""
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            dialog2.open = False
            huecod.value = ""
            admcod.value = ""
            habcod.value = ""
            fecentaño.value = ""
            fecentmes.value = ""
            fecentdia.value = ""
            fecsalaño.value = ""
            fecsalmes.value = ""
            fecsaldia.value = ""
            resest.value = ""
            page.update()
            
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
            huecod,
            admcod,
            habcod,
            fecentaño,
            fecentmes,
            fecentdia,
            fecsalaño,
            fecsalmes,
            fecsaldia,
            resest,
            # esttxt
        ],
        scroll=ft.ScrollMode.ALWAYS),
        actions = [
            TextButton("AGREGAR", on_click=addtodb),
            TextButton("CANCELAR", on_click=cancelIn),
        ]
    )

    #Boton redireccionamiento
    def AddBtn(e):
        huecod.value = ""
        admcod.value = ""
        habcod.value = ""
        fecentaño.value = ""
        fecentmes.value = ""
        fecentdia.value = ""
        fecsalaño.value = ""
        fecsalmes.value = ""
        fecsaldia.value = ""
        resest.value = ""
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
    
    #Main
    page.title = "RESERVA"
    page.window_maximized = True
    page.add(
        AppBar(
            title = Text("TABLA RESERVA", size = 30),
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
        ft.Divider(),
        Container(mydt, alignment=ft.alignment.center),
        
    )
    
ft.app(target=main)