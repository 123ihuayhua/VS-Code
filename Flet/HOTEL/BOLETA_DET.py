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
    huecod = TextField(label="Huesped Código")  
    admcod = TextField(label="Administrador Código") 
    habcod = TextField(label="Habitación Código") 
    bolfecentaño = TextField(label="Año Entrada")  
    bolfecentmes = TextField(label="Mes Entrada")  
    bolfecentdia = TextField(label="Día Entrada")  
    bolfecsalaño = TextField(label="Año Salida")  
    bolfecsalmes = TextField(label="Mes Salida")  
    bolfecsaldia = TextField(label="Día Salida") 
    boldescat = TextField(label="Descripción Categoría Habitación")
    rent = TextField(label="Renta")
    total = TextField(label="Total")

    # Editar
    edit_codtxt = TextField(label="Código", disabled=True)
    edit_huecod = TextField(label="Huesped")  
    edit_admcod = TextField(label="Administrador Código") 
    edit_habcod = TextField(label="Habitación Código")  
    edit_bolfecentaño = TextField(label="Año Entrada")  
    edit_bolfecentmes = TextField(label="Mes Entrada")  
    edit_bolfecentdia = TextField(label="Día Entrada")
    edit_bolfecsalaño = TextField(label="Año Salida")  
    edit_bolfecsalmes = TextField(label="Mes Salida")  
    edit_bolfecsaldia = TextField(label="Día Salida")  
    edit_boldescat = TextField(label="Descripción Categoría Habitación")
    edit_rent = TextField(label="Renta")
    edit_total = TextField(label="Total")  
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
            DataColumn(Text("Huesped")),
            DataColumn(Text("Administrador")),
            DataColumn(Text("Habitación")),
            DataColumn(Text("Año E.")),
            DataColumn(Text("Mes E.")),
            DataColumn(Text("Día E.")),
            DataColumn(Text("Año S.")),
            DataColumn(Text("Mes S.")),
            DataColumn(Text("Día S.")),
            DataColumn(Text("Descripción")),
            DataColumn(Text("Renta")),
            DataColumn(Text("Total")),
            DataColumn(Text("E.R")),
            DataColumn(Text("Acciones")),
        ],
        rows=[]
    )

    # Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE BOLETA_DETALLE SET BolDetHueCod = %s, BolDetAdmCod = %s, BolDetHabCod = %s, BolDetFecEntAño = %s, BolDetFecEntMes = %s, BolDetFecEntDia = %s, BolDetFecSalAño = %s, BolDetFecSalMes = %s, BolDetFecSalDia = %s, BolDetCatHabDes = %s, BolDetRen = %s, BolDetTot=%s WHERE BolDetCod = %s"
            val = (edit_huecod.value, edit_admcod.value, edit_habcod.value, edit_bolfecentaño.value, edit_bolfecentmes.value, edit_bolfecentdia.value, edit_bolfecsalaño.value, edit_bolfecsalmes.value, edit_bolfecsaldia.value, edit_boldescat.value, edit_rent.value, edit_total.value, edit_codtxt.value)
            cursor.execute(sql, val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            # Limipiar campos
            edit_huecod.value = ""
            edit_admcod.value = ""
            edit_habcod.value = ""
            edit_bolfecentaño.value = ""
            edit_bolfecentmes.value = ""
            edit_bolfecentdia.value = ""
            edit_bolfecsalaño.value = ""
            edit_bolfecsalmes.value = ""
            edit_bolfecsaldia.value = ""
            edit_boldescat.value = ""
            edit_rent.value = ""
            edit_total.value = ""
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
            sql = "UPDATE BOLETA_DETALLE SET BolDetEstReg = %s WHERE BolDetCod = %s"
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
            edit_huecod.value = ""
            edit_admcod.value = ""
            edit_habcod.value = ""
            edit_bolfecentaño.value = ""
            edit_bolfecentmes.value = ""
            edit_bolfecentdia.value = ""
            edit_bolfecsalaño.value = ""
            edit_bolfecsalmes.value = ""
            edit_bolfecsaldia.value = ""
            edit_boldescat.value = ""
            edit_rent.value = ""
            edit_total.value = ""
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
            edit_huecod,
            edit_admcod,
            edit_habcod,
            edit_bolfecentaño,
            edit_bolfecentmes,
            edit_bolfecentdia,
            edit_bolfecsalaño,
            edit_bolfecsalmes,
            edit_bolfecsaldia,
            edit_boldescat,
            edit_rent,
            edit_total,
            edit_esttxt]),
        actions=[
            TextButton("Guardar", on_click=savedata),
            TextButton("Cancelar", on_click=cancelform),
            TextButton("Inactivar", on_click=inactbtn)]
    )

    #Editar
    def createbtn(e):
        edit_codtxt.value = e.control.data['BolDetCod']
        edit_huecod.value = e.control.data['BolDetHueCod']
        edit_admcod.value = e.control.data['BolDetAdmCod']
        edit_habcod.value = e.control.data['BolDetHabCod']
        edit_bolfecentaño.value = e.control.data['BolDetFecEntAño']
        edit_bolfecentmes.value = e.control.data['BolDetFecEntMes']
        edit_bolfecentdia.value = e.control.data['BolDetFecEntDia']
        edit_bolfecsalaño.value = e.control.data['BolDetFecSalAño']
        edit_bolfecsalmes.value = e.control.data['BolDetFecSalMes']
        edit_bolfecsaldia.value = e.control.data['BolDetFecSalDia']
        edit_boldescat.value = e.control.data['BolDetCatHabDes']
        edit_rent.value = e.control.data['BolDetRen']
        edit_total.value = e.control.data['BolDetTot']
        edit_esttxt.value = e.control.data['BolDetEstReg']

        page.dialog = dialog
        dialog.open = True
        page.update()

    # Activar Registro
    def actbtn(e):
        try:
            sql = "UPDATE BOLETA_DETALLE SET BolDetEstReg = %s WHERE BolDetCod = %s"
            val = ('A', e.control.data['BolDetCod'])
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
            sql = "UPDATE BOLETA_CABECERA SET BolDetEstReg = %s WHERE BolDetCod = %s"
            val = ('*', e.control.data['BolDetCod'])
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
        cursor.execute("SELECT * FROM BOLETA_DETALLE")
        result = cursor.fetchall()
        # Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        # Bucle de pusheo
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['BolDetCod'])),
                        DataCell(Text(row['BolDetHueCod'])),
                        DataCell(Text(row['BolDetAdmCod'])),
                        DataCell(Text(row['BolDetHabCod'])),
                        DataCell(Text(row['BolDetFecEntAño'])),
                        DataCell(Text(row['BolDetFecEntMes'])),
                        DataCell(Text(row['BolDetFecEntDia'])),
                        DataCell(Text(row['BolDetFecSalAño'])),
                        DataCell(Text(row['BolDetFecSalMes'])),
                        DataCell(Text(row['BolDetFecSalDia'])),
                        DataCell(Text(row['BolDetCatHabDes'])),
                        DataCell(Text(row['BolDetRen'])),
                        DataCell(Text(row['BolDetTot'])),
                        DataCell(Text(row['BolDetEstReg'])),
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
            if (row['BolDetEstReg'] == 'I' or row['BolDetEstReg'] == '*'):
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
            sql = "INSERT INTO boleta_detalle (BolDetCod, BolDetHueCod, BolDetAdmCod,  BolDetHabCod,  BolDetFecEntAño,  BolDetFecEntMes,  BolDetFecEntDia,  BolDetFecSalAño, BolDetFecSalMes, BolDetFecSalDia, BolDetCatHabDes,  BolDetRen,  BolDetTot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (codtxt.value, huecod.value, admcod.value, habcod.value, bolfecentaño.value, bolfecentmes.value, bolfecentdia.value, bolfecsalaño.value, bolfecsalmes.value, bolfecsaldia.value, boldescat.value, rent.value, total.value, )
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
        admcod.value = ""
        huecod.value = ""
        bolfecentaño.value = ""
        bolfecentmes.value = ""
        bolfecentdia.value = ""
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            dialog2.open = False
            codtxt.value = ""
            admcod.value = ""
            huecod.value = ""
            bolfecentaño.value = ""
            bolfecentmes.value = ""
            bolfecentdia.value = ""
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
            admcod,
            huecod,
            bolfecentaño,
            bolfecentmes,
            bolfecentdia,
            bolfecsalaño,
            bolfecsalmes,
            bolfecsaldia,
            boldescat,
            rent,
            total,
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
        huecod.value =  "" 
        admcod.value = ""
        habcod.value = ""
        bolfecentaño.value = ""  
        bolfecentmes.value = ""  
        bolfecentdia.value = ""  
        bolfecsalaño.value = ""  
        bolfecsalmes.value = ""
        bolfecsaldia.value = "" 
        boldescat.value = ""
        rent.value = ""
        total.value = ""
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
    page.title = "BOLETA DETALLE"
    page.window_height = 1080
    page.window_width = 1600
    page.add(
        AppBar(
            title = Text("TABLA BOLETA DETALLE", size = 30),
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