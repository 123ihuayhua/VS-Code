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
    # Agregar HOTEL
    cod = TextField(label="Código") 
    ruc = TextField(label="RUC")
    nomhot = TextField(label="Nombre Hotel")  
    apepat = TextField(label="Apellido Paterno Dueño") 
    apemat = TextField(label="Apellido Materno Dueño")  
    nom = TextField(label="Nombre Dueño")  

    # Editar
    edit_cod = TextField(label="Código", disabled=True)
    edit_ruc = TextField(label="RUC")  
    edit_nomhot = TextField(label="Nombre Hotel")  
    edit_apepat = TextField(label="Apellido Paterno Dueño")  
    edit_apemat = TextField(label="Apellido Materno Dueño")  
    edit_nom = TextField(label="Nombre Dueño")
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
            DataColumn(Text("RUC")),
            DataColumn(Text("Nombre Hotel")),
            DataColumn(Text("Apellido Paterno Dueño")),
            DataColumn(Text("Apellido Materno Dueño")),
            DataColumn(Text("Nombre Dueño")),
            DataColumn(Text("Estado de Registro")),
            DataColumn(Text("Acciones")),
        ],
        rows=[]
    )

    # Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE HOTEL SET HotRUC = %s, HotNom = %s, HotApePatDue = %s, HotApeMatDue = %s, HotNomDue = %s, HotEstReg = %s WHERE HotCod = %s"
            val = (edit_ruc.value, edit_nomhot.value, edit_apepat.value, edit_apemat.value, edit_nom.value, edit_esttxt.value, edit_cod.value)
            cursor.execute(sql, val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            # Limipiar campos
            edit_ruc.value = ""
            edit_nomhot.value = ""
            edit_apepat.value = ""
            edit_apemat.value = ""
            edit_nom.value = ""
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
            sql = "UPDATE HOTEL SET HotEstReg = %s WHERE HotCod = %s"
            val = ('I', edit_cod.value)
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
            edit_ruc.value = ""
            edit_nomhot.value = ""
            edit_apepat.value = ""
            edit_apemat.value = ""
            edit_nom.value = ""
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
            edit_cod,
            edit_ruc,
            edit_nomhot,
            edit_apepat,
            edit_apemat,
            edit_nom,
            edit_esttxt]),
        actions=[
            TextButton("Guardar", on_click=savedata),
            TextButton("Cancelar", on_click=cancelform),
            TextButton("Inactivar", on_click=inactbtn)]
    )

    #Editar
    def createbtn(e):
        edit_cod.value = e.control.data['HotCod']
        edit_ruc.value = e.control.data['HotRUC']
        edit_nomhot.value = e.control.data['HotNom']
        edit_apepat.value = e.control.data['HotApePatDue']
        edit_apemat.value = e.control.data['HotApeMatDue']
        edit_nom.value = e.control.data['HotNomDue']
        edit_esttxt.value = e.control.data['HotEstReg']

        page.dialog = dialog
        dialog.open = True
        page.update()

    # Activar Registro
    def actbtn(e):
        try:
            sql = "UPDATE HOTEL SET HotEstReg = %s WHERE HotCod = %s"
            val = ('A', e.control.data['HotCod'])
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
            sql = "UPDATE HOTEL SET HotEstReg = %s WHERE HotCod = %s"
            val = ('*', e.control.data['HotCod'])
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
        cursor.execute("SELECT * FROM HOTEL")
        result = cursor.fetchall()
        # Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        # Bucle de pusheo
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['HotCod'])),
                        DataCell(Text(row['HotRUC'])),
                        DataCell(Text(row['HotNom'])),
                        DataCell(Text(row['HotApePatDue'])),
                        DataCell(Text(row['HotApeMatDue'])),
                        DataCell(Text(row['HotNomDue'])),
                        DataCell(Text(row['HotEstReg'])),
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
            if (row['HotEstReg'] == 'I' or row['HotEstReg'] == '*'):
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
            sql = "INSERT INTO HOTEL (HotCod, HotRUC, HotNom, HotApePatDue, HotApeMatDue, HotNomDue) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (cod.value, ruc.value, nomhot.value, apepat.value, apemat.value, nom.value,)
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
        cod.value = ""
        ruc.value = ""
        nomhot.value = ""
        apepat.value = ""
        apemat.value = ""
        nom.value = ""
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            dialog2.open = False
            cod.value = ""
            ruc.value = ""
            nomhot.value = ""
            apepat.value = ""
            apemat.value = ""
            nom.value = ""
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
            cod,
            ruc,
            nomhot,
            apepat,
            apemat,
            nom,
            # esttxt
        ]),
        actions = [
            TextButton("AGREGAR", on_click=addtodb),
            TextButton("CANCELAR", on_click=cancelIn),
        ]
    )

    #Boton redireccionamiento
    def AddBtn(e):
        cod.value = ""
        ruc.value = ""
        nomhot.value = ""
        apepat.value = ""
        apemat.value = ""
        nom.value = ""
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
    page.title = "HOTEL"
    page.window_height = 1080
    page.window_width = 1600
    page.add(
        AppBar(
            title = Text("TABLA HOTEL", size = 30),
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