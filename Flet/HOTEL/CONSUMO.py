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
    # Agregar CONSUMO
    codpro = TextField(label="Código Producto")
    codadm = TextField(label="Administrador")  
    codhue = TextField(label="Huesped")
    codhab = TextField(label="Habitación")
    fecaño = TextField(label="Año")  
    fecmes = TextField(label="Mes")  
    fecdia = TextField(label="Día")  
    preuni = TextField(label="Precio Unitario")  
    procan = TextField(label="Cantidad")  
    estpro = TextField(label="Estado Producto")  

    # Editar
    edit_codpro = TextField(label="Código Producto", disabled = True)
    edit_codadm = TextField(label="Administrador")  
    edit_codhue = TextField(label="Huesped")
    edit_codhab = TextField(label="Habitación")
    edit_fecaño = TextField(label="Año")  
    edit_fecmes = TextField(label="Mes")  
    edit_fecdia = TextField(label="Día")  
    edit_preuni = TextField(label="Precio Unitario")  
    edit_procan = TextField(label="Cantidad")  
    edit_estpro = TextField(label="Estado Producto") 
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
            DataColumn(Text("Producto")),
            DataColumn(Text("Administrador")),
            DataColumn(Text("Huesped")),
            DataColumn(Text("Habitación")),
            DataColumn(Text("Año")),
            DataColumn(Text("Mes")),
            DataColumn(Text("Día")),
            DataColumn(Text("Precio Unitario")),
            DataColumn(Text("Cantidad")),
            DataColumn(Text("Estado Producto")),
            DataColumn(Text("Estado de Registro")),
            DataColumn(Text("Acciones")),
        ],
        rows=[]
    )

    # Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE CONSUMO SET ConAdmCod = %s, ConHueCod = %s, ConHabCod = %s, ConFecAño = %s, ConFecMes = %s, ConFecDia = %s, ConPreUni = %s, ConProCan = %s, ConEstPro = %s, ConEstReg = %s WHERE ConCodPro = %s"
            val = (edit_codadm.value, edit_codhue.value, edit_codhab.value, edit_fecaño.value, edit_fecmes.value, edit_fecdia.value, edit_preuni.value,edit_procan.value, edit_estpro.value, edit_esttxt.value, edit_codpro.value)
            cursor.execute(sql, val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            # Limipiar campos
            edit_codadm.value = ""
            edit_codhue.value = ""
            edit_codhab.value = ""
            edit_fecaño.value = ""
            edit_fecmes.value = ""
            edit_fecdia.value = ""
            edit_preuni.value = ""
            edit_procan.value = ""
            edit_estpro.value = ""
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
            sql = "UPDATE CONSUMO SET ConEstReg = %s WHERE ConCodPro = %s"
            val = ('I', edit_codpro.value)
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
            edit_codadm.value = ""
            edit_codhue.value = ""
            edit_codhab.value = ""
            edit_fecaño.value = ""
            edit_fecmes.value = ""
            edit_fecdia.value = ""
            edit_preuni.value = ""
            edit_procan.value = ""
            edit_estpro.value = ""
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
            edit_codpro,
            edit_codadm,
            edit_codhue,
            edit_codhab,
            edit_fecaño,
            edit_fecmes,
            edit_fecdia,
            edit_preuni,
            edit_procan,
            edit_estpro,
            edit_esttxt]),
        actions=[
            TextButton("Guardar", on_click=savedata),
            TextButton("Cancelar", on_click=cancelform),
            TextButton("Inactivar", on_click=inactbtn)]
    )

    #Editar
    def createbtn(e):
        edit_codpro.value = e.control.data['ConCodPro']
        edit_codadm.value = e.control.data['ConAdmCod']
        edit_codhue.value = e.control.data['ConHueCod']
        edit_codhab.value = e.control.data['ConHabCod']
        edit_fecaño.value = e.control.data['ConFecAño']
        edit_fecmes.value = e.control.data['ConFecMes']
        edit_fecdia.value = e.control.data['ConFecDia']
        edit_preuni.value = e.control.data['ConPreUni']
        edit_procan.value = e.control.data['ConProCan']
        edit_estpro.value = e.control.data['ConEstPro']
        edit_esttxt.value = e.control.data['ConEstReg']

        page.dialog = dialog
        dialog.open = True
        page.update()

    # Activar Registro
    def actbtn(e):
        try:
            sql = "UPDATE CONSUMO SET ConEstReg = %s WHERE ConCodPro = %s"
            val = ('A', e.control.data['ConCodPro'])
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
            sql = "UPDATE CONSUMO SET ConEstReg = %s WHERE ConCodPro = %s"
            val = ('*', e.control.data['ConCodPro'])
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
        cursor.execute("SELECT * FROM CONSUMO")
        result = cursor.fetchall()
        # Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        # Bucle de pusheo
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['ConCodPro'])),
                        DataCell(Text(row['ConAdmCod'])),
                        DataCell(Text(row['ConHueCod'])),
                        DataCell(Text(row['ConHabCod'])),
                        DataCell(Text(row['ConFecAño'])),
                        DataCell(Text(row['ConFecMes'])),
                        DataCell(Text(row['ConFecDia'])),
                        DataCell(Text(row['ConPreUni'])),
                        DataCell(Text(row['ConProCan'])),
                        DataCell(Text(row['ConEstPro'])),
                        DataCell(Text(row['ConEstReg'])),
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
            if (row['ConEstReg'] == 'I' or row['ConEstReg'] == '*'):
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
            sql = "INSERT INTO CONSUMO (ConCodPro, ConAdmCod, ConHueCod, ConHabCod, ConFecAño, ConFecMes, ConFecDia, ConPreUni, ConProCan, ConEstPro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (codpro.value, codadm.value, codhue.value, codhab.value, fecaño.value, fecmes.value, fecdia.value, preuni.value, procan.value, estpro.value,)
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
        codpro.value = ""
        codadm.value = ""
        codhue.value = ""
        codhab.value = ""
        fecaño.value = ""
        fecmes.value = ""
        fecdia.value = ""
        preuni.value = ""
        procan.value = ""
        estpro.value = ""
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            dialog2.open = False
            codpro.value = ""
            codadm.value = ""
            codhue.value = ""
            codhab.value = ""
            fecaño.value = ""
            fecmes.value = ""
            fecdia.value = ""
            preuni.value = ""
            procan.value = ""
            estpro.value = ""
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
            codpro,
            codadm,
            codhue,
            codhab,
            fecaño,
            fecmes,
            fecdia,
            preuni,
            procan,
            estpro,
            # esttxt
        ]),
        actions = [
            TextButton("AGREGAR", on_click=addtodb),
            TextButton("CANCELAR", on_click=cancelIn),
        ]
    )

    #Boton redireccionamiento
    def AddBtn(e):
        codpro.value = ""
        codadm.value = ""
        codhue.value = ""
        codhab.value = ""
        fecaño.value = ""
        fecmes.value = ""
        fecdia.value = ""
        preuni.value = ""
        procan.value = ""
        estpro.value = ""
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
    page.title = "CONSUMO"
    page.window_height = 1080
    page.window_width = 1600
    page.add(
        AppBar(
            title = Text("TABLA CONSUMO", size = 30),
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