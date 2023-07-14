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
    # Agregar ADMIN_TURNO
    codtxt = TextField(label="Código")
    hotcodtxt = TextField(label="Hotel Código")  
    clicodtxt = TextField(label="Cliente Código")  
    bolfecaño = TextField(label="Año Emisión")  
    bolfecmes = TextField(label="Mes Emisión")  
    bolfecdia = TextField(label="Día Emisión")  

    # Editar
    edit_codtxt = TextField(label="Código", disabled=True)
    edit_hotcodtxt = TextField(label="Hotel Código", disabled=True)  
    edit_clicodtxt = TextField(label="Cliente Código")  
    edit_bolfecaño = TextField(label="Año Emisión")  
    edit_bolfecmes = TextField(label="Mes Emisión")  
    edit_bolfecdia = TextField(label="Día Emisión")   
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
            DataColumn(Text("Hotel Código")),
            DataColumn(Text("Cliente Código")),
            DataColumn(Text("Año Emisión")),
            DataColumn(Text("Mes Emisión")),
            DataColumn(Text("Día Emisión")),
            DataColumn(Text("Estado de Registro")),
            DataColumn(Text("Acciones")),
        ],
        rows=[]
    )

    # Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE BOLETA_CABECERA SET BolCabCliCod = %s, BolCabFecAño = %s, BolCabFecMes = %s, BolCabFecDia = %s WHERE BolCabCod = %s"
            val = (edit_clicodtxt.value, edit_bolfecaño.value, edit_bolfecmes.value, edit_bolfecdia.value, edit_codtxt.value)
            cursor.execute(sql, val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            # Limipiar campos
            edit_clicodtxt.value = ""
            edit_bolfecaño.value = ""
            edit_bolfecmes.value = ""
            edit_bolfecdia.value = ""
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
            sql = "UPDATE BOLETA_CABECERA SET BolCabEstReg = %s WHERE BolCabCod = %s"
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
            # Limpiar campos
            edit_clicodtxt.value = ""
            edit_bolfecaño.value = ""
            edit_bolfecmes.value = ""
            edit_bolfecdia.value = ""
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
            edit_hotcodtxt,
            edit_clicodtxt,
            edit_bolfecaño,
            edit_bolfecmes,
            edit_bolfecdia,
            edit_esttxt]),
        actions=[
            TextButton("Guardar", on_click=savedata),
            TextButton("Cancelar", on_click=cancelform),
            TextButton("Inactivar", on_click=inactbtn)]
    )

    #Editar
    def createbtn(e):
        edit_codtxt.value = e.control.data['BolCabCod']
        edit_hotcodtxt.value = e.control.data['BolCabHotCod']
        edit_clicodtxt.value = e.control.data['BolCabCliCod']
        edit_bolfecaño.value = e.control.data['BolCabFecAño']
        edit_bolfecmes.value = e.control.data['BolCabFecMes']
        edit_bolfecdia.value = e.control.data['BolCabFecDia']
        edit_esttxt.value = e.control.data['BolCabEstReg']

        page.dialog = dialog
        dialog.open = True
        page.update()

    # Activar Registro
    def actbtn(e):
        try:
            sql = "UPDATE BOLETA_CABECERA SET BolCabEstReg = %s WHERE BolCabCod = %s"
            val = ('A', e.control.data['BolCabCod'])
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
            sql = "UPDATE BOLETA_CABECERA SET BolCabEstReg = %s WHERE BolCabCod = %s"
            val = ('*', e.control.data['BolCabCod'])
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
        cursor.execute("SELECT * FROM BOLETA_CABECERA")
        result = cursor.fetchall()
        # Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        # Bucle de pusheo
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['BolCabCod'])),
                        DataCell(Text(row['BolCabHotCod'])),
                        DataCell(Text(row['BolCabCliCod'])),
                        DataCell(Text(row['BolCabFecAño'])),
                        DataCell(Text(row['BolCabFecMes'])),
                        DataCell(Text(row['BolCabFecDia'])),
                        DataCell(Text(row['BolCabEstReg'])),
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
            if (row['BolCabEstReg'] == 'I' or row['BolCabEstReg'] == '*'):
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
            sql = "INSERT INTO BOLETA_CABECERA (BolCabCod, BolCabHotCod, BolCabCliCod, BolCabFecAño, BolCabFecMes, BolCabFecDia) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (codtxt.value, hotcodtxt.value, clicodtxt.value, bolfecaño.value, bolfecmes.value, bolfecdia.value,)
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
        hotcodtxt.value = ""
        clicodtxt.value = ""
        bolfecaño.value = ""
        bolfecmes.value = ""
        bolfecdia.value = ""
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            dialog2.open = False
            codtxt.value = ""
            hotcodtxt.value = ""
            clicodtxt.value = ""
            bolfecaño.value = ""
            bolfecmes.value = ""
            bolfecdia.value = ""
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
            codtxt,
            hotcodtxt,
            clicodtxt,
            bolfecaño,
            bolfecmes,
            bolfecdia,
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
        hotcodtxt.value = ""
        clicodtxt.value = ""
        bolfecaño.value = ""
        bolfecmes.value = ""
        bolfecdia.value = ""
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
    page.title = "BOLETA CABECERA"
    page.window_maximized = True
    page.add(
        AppBar(
            title = Text("TABLA BOLETA CABECERA", size = 30),
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