from flet import *
import flet as ft
import mysql.connector

#Conexión BD
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    port = 3306,
    password = 'lm10kayca', #contraseña
    database = 'hotel'
)
cursor = mydb.cursor()
def main(page:Page):
    page.scroll = "always"
    page.update()
    #Agregar 
    codtxt = TextField(label="Código")
    dnitxt = TextField(label="DNI")
    apeptxt = TextField(label="Apellido Paterno")
    apemtxt = TextField(label="Apellido Materno")
    nametxt = TextField(label="Nombre")
    teltxt = TextField(label="Teléfono")
    esttxt = TextField(label="Estado de Registro")

    #Editar 
    edit_codtxt = TextField(label="Código")
    edit_dnitxt = TextField(label="DNI")
    edit_apeptxt = TextField(label="Apellido Paterno")
    edit_apemtxt = TextField(label="Apellido Materno")
    edit_nametxt = TextField(label="Nombre")
    edit_teltxt = TextField(label="Teléfono")
    edit_esttxt = TextField(label="Estado de Registro")

    mydt = DataTable(
        columns=[
            DataColumn(Text("Código")),
            DataColumn(Text("DNI")),
            DataColumn(Text("Apellido Paterno")),
            DataColumn(Text("Apellido Materno")),
            DataColumn(Text("Nombre")),
            DataColumn(Text("Teléfono")),
            DataColumn(Text("Estado de Registro")),
            DataColumn(Text("Acciones")),
        ], 
        rows=[]
    )

    #Eliminar elementos
    def deletebtn(e):
        print("El código seleccionado es: ", e.control.data['HueCod'])
        try:
            sql = "DELETE FROM huesped WHERE HueCod = %s"
            val = (e.control.data['HueCod'],)
            cursor.execute(sql,val)
            mydb.commit()
            print("Huesped Eliminado")
            mydt.rows.clear()
            load_data()
            page.snack_bar = SnackBar(
                Text("Dato eliminado", size=15),
                bgcolor="red",
            )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print("Error en el código para eliminar")

    #Boton Guardado
    def savedata(e):
        try:
            sql = "UPDATE huesped SET HueDNI = %s, HueApePat = %s, HueApeMat = %s, HueNom = %s, HuerTel = %s, HueEstReg = %s WHERE HueCod = %s"
            val = (edit_dnitxt.value, edit_apeptxt.value, edit_apemtxt.value, edit_nametxt.value, edit_teltxt.value, edit_esttxt.value, edit_codtxt.value)
            cursor.execute(sql,val)
            mydb.commit()
            print("Edición exitosa!")
            dialog.open = False
            page.update()

            #Limipiar campos
            edit_codtxt.value = ""
            edit_dnitxt.value = ""         
            edit_apeptxt.value = ""
            edit_apemtxt.value = ""
            edit_nametxt.value = ""          
            edit_teltxt.value = ""          
            edit_esttxt.value = ""

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
    
    #Cuadro de diálogo
    dialog = AlertDialog(
        title=Text("Edit Data"),
        content=Column([
            edit_dnitxt,
            edit_apeptxt,
            edit_apemtxt,
            edit_nametxt,
            edit_teltxt,
            edit_esttxt,]),
        actions=[
            TextButton("Guardado", on_click=savedata)]
    )
    
    def createbtn(e):
        edit_codtxt.value  = e.control.data['HueCod']
        edit_dnitxt.value = e.control.data['HueDNI']
        edit_apeptxt.value = e.control.data['HueApePat']
        edit_apemtxt.value = e.control.data['HueApeMat']
        edit_nametxt.value = e.control.data['HueNom']
        edit_teltxt.value = e.control.data['HuerTel']
        edit_esttxt.value = e.control.data['HueEstReg']
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    #Animación
    def toggle_icon_button(e):
        e.control.selected = not e.control.selected
        e.control.update()
        
        if e.control.selected:
            inactbtn(e)
        else:
            actbtn(e)
        
        e.control.update()

    #Activar Registro
    def actbtn(e):
        try:
            sql = "UPDATE huesped SET HueEstReg = %s WHERE HueCod = %s"
            val = ('A', e.control.data['HueCod'])
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

    #Desactivar registro
    def inactbtn(e):
        try:
            sql = "UPDATE huesped SET HueEstReg = %s WHERE HueCod = %s"
            val = ('I', e.control.data['HueCod'])
            cursor.execute(sql, val)
            mydb.commit()
            print("Registro Inactivado")
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
    
    #Eliminado lógico
    def dellog(e):
        try:
            sql = "UPDATE huesped SET HueEstReg = %s WHERE HueCod = %s"
            val = ('*', e.control.data['HueCod'])
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
        cursor.execute("SELECT * FROM huesped")
        result = cursor.fetchall()
        #Push al diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        #Bucle de pusheo 
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['HueCod'])),
                        DataCell(Text(row['HueDNI'])),
                        DataCell(Text(row['HueApePat'])),
                        DataCell(Text(row['HueApeMat'])),
                        DataCell(Text(row['HueNom'])),
                        DataCell(Text(row['HuerTel'])),
                        DataCell(Text(row['HueEstReg'])),
                        DataCell(
                            Row([
                                IconButton("delete", icon_color='red',
                                        data=row,
                                        on_click=deletebtn),
                                IconButton("create", icon_color='blue',
                                        data=row,
                                        on_click=createbtn),
                                IconButton("check_box", icon_color='green',
                                        data=row,
                                        on_click=actbtn),
                                IconButton("check_box_outline_blank", icon_color='green',
                                        data=row,
                                        on_click=inactbtn),
                                IconButton("stars", icon_color='yellow',
                                        data=row,
                                        on_click=dellog),
                                # ft.IconButton(
                                #     icon = ft.icons.CHECK_BOX,
                                #     selected_icon = ft.icons.CHECK_BOX_OUTLINE_BLANK,
                                #     on_click=toggle_icon_button,
                                #     selected= False,
                                #     style=ft.ButtonStyle(color={"selected": ft.colors.RED, "": ft.colors.GREEN}),
                                #)
                            ])
                        )
                    ]
                )
            )
            page.update()


    #Llamar función cuando la aplicación está abierta
    load_data()

    def addtodb(e):
        try: 
            sql = "INSERT INTO huesped (HueCod, HueDNI, HueApePat, HueApeMat, HueNom, HuerTel, HueEstReg) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (codtxt.value, dnitxt.value, apeptxt.value, apemtxt.value, nametxt.value, teltxt.value, esttxt.value)
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
        dnitxt.value = "" 
        apeptxt.value = "" 
        apemtxt.value = "" 
        nametxt.value = "" 
        teltxt.value = "" 
        esttxt.value = ""
        page.update()
    
    #Cancelar registro
    def cancelIn(e):
        try:
            codtxt.value = ""
            dnitxt.value = "" 
            apeptxt.value = "" 
            apemtxt.value = "" 
            nametxt.value = "" 
            teltxt.value = "" 
            esttxt.value = ""
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

    #Funcióm scrollbar
    def scrollfuc(e:OnScrollEvent):
        print(e)
    
    
    page.add(
        Column([
            codtxt, dnitxt, apeptxt, apemtxt, nametxt, teltxt, esttxt,
            Row([
                ElevatedButton("AGREGAR", on_click=addtodb),
                ElevatedButton("CANCELAR", on_click=cancelIn),
            ]),
            mydt,
            ], 
        ),
    )
    
flet.app(target=main)