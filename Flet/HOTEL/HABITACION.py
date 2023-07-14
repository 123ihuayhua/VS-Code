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
    # Agregar HABITACION
    habcod = TextField(label="Código Habitación")
    habcatcod = TextField(label="Código Categoría Habitación")  
    habpis = TextField(label="Piso Habitación")
    habnum = TextField(label="Número Habitación")  

    # Editar
    edit_habcod = TextField(label="Código Habitación", disabled=True)
    edit_habcatcod = TextField(label="Código Categoría Habitación")  
    edit_habpis = TextField(label="Piso Habitación")
    edit_habnum = TextField(label="Número Habitación") 
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
            DataColumn(Text("Cod. Categoría")),
            DataColumn(Text("Piso")),
            DataColumn(Text("Número")),
            DataColumn(Text("Estado de Registro")),
            DataColumn(Text("Acciones")),
        ],
        rows=[]
    )

    # Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE HABITACION SET HabCatCod = %s, HabPis = %s, HabNumHab = %s, HabEstReg = %s WHERE HabCod = %s"
            val = (edit_habcatcod.value, edit_habpis.value, edit_habnum.value, edit_esttxt.value, edit_habcod.value)
            cursor.execute(sql, val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            # Limipiar campos
            edit_habcatcod.value = ""
            edit_habpis.value = ""
            edit_habnum.value = ""
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
            sql = "UPDATE HABITACION SET HabEstReg = %s WHERE HabCod = %s"
            val = ('I', edit_habcod.value)
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
            edit_habcatcod.value = ""
            edit_habpis.value = ""
            edit_habnum.value = ""
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
            edit_habcod,
            edit_habcatcod,
            edit_habpis,
            edit_habnum,
            edit_esttxt]),
        actions=[
            TextButton("Guardar", on_click=savedata),
            TextButton("Cancelar", on_click=cancelform),
            TextButton("Inactivar", on_click=inactbtn)]
    )

    #Editar
    def createbtn(e):
        edit_habcod.value = e.control.data['HabCod']
        edit_habcatcod.value = e.control.data['HabCatCod']
        edit_habpis.value = e.control.data['HabPis']
        edit_habnum.value = e.control.data['HabNumHab']
        edit_esttxt.value = e.control.data['HabEstReg']

        page.dialog = dialog
        dialog.open = True
        page.update()

    # Activar Registro
    def actbtn(e):
        try:
            sql = "UPDATE HABITACION SET HabEstReg = %s WHERE HabCod = %s"
            val = ('A', e.control.data['HabCod'])
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
            sql = "UPDATE HABITACION SET HabEstReg = %s WHERE HabCod = %s"
            val = ('*', e.control.data['HabCod'])
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
        cursor.execute("SELECT * FROM HABITACION")
        result = cursor.fetchall()
        # Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        # Bucle de pusheo
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['HabCod'])),
                        DataCell(Text(row['HabCatCod'])),
                        DataCell(Text(row['HabPis'])),
                        DataCell(Text(row['HabNumHab'])),
                        DataCell(Text(row['HabEstReg'])),
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
            if (row['HabEstReg'] == 'I' or row['HabEstReg'] == '*'):
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
            sql = "INSERT INTO habitacion (HabCod, HabCatCod, HabPis, HabNumHab) VALUES (%s, %s, %s, %s)"
            val = (habcod.value, habcatcod.value, habpis.value, habnum.value,)
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
        habcod.value = ""
        habcatcod.value = ""
        habpis.value = ""
        habnum.value = ""
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            dialog2.open = False
            habcod.value = ""
            habcatcod.value = ""
            habpis.value = ""
            habnum.value = ""
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
            habcod,
            habcatcod,
            habpis,
            habnum,
            # esttxt
        ]),
        actions = [
            TextButton("AGREGAR", on_click=addtodb),
            TextButton("CANCELAR", on_click=cancelIn),
        ]
    )

    #Boton redireccionamiento
    def AddBtn(e):
        habcod.value = ""
        habcatcod.value = ""
        habpis.value = ""
        habnum.value = ""
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
    page.title = "HABITACION"
    page.window_maximized = True
    page.add(
        AppBar(
            title = Text("TABLA HABITACION", size = 30),
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