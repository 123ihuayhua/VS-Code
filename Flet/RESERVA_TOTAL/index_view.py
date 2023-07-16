
import time
import flet as ft
from flet import *

def IndexView(page):
    page.scroll = "always"
    #Reserva elementos
    huecod = TextField(label="Huesped", width=400)
    admcod = TextField(label="Administrador", width=400)  
    habcod = TextField(label="Habitación", width=400)  
    fecentaño = TextField(label="Año", width=120)  
    fecentmes = TextField(label="Mes", width=120)  
    fecentdia = TextField(label="Dia", width=120)  
    fecsalaño = TextField(label="Año", width=120)  
    fecsalmes = TextField(label="Mes", width=120)  
    fecsaldia = TextField(label="Dia", width=120)  
    resest = TextField(label="Estado Reserva", width=200)

    #Vista Huesped
    dni = TextField(label="DNI",width=400)
    apepat = TextField(label="Apellido Paterno",width=400)  
    apemat = TextField(label="Apellido Materno",width=400)  
    nom = TextField(label="Nombre",width=400)  
    tel = TextField(label="Teléfono",width=400)

    #Vista habitación
    habcatcod = Dropdown(label="Categoría Habitación",width=400,
                         options=[
                             dropdown.Option("SIMPLE"),
                             dropdown.Option("DOBLE"),
                             dropdown.Option("TRIPLE"),
                             dropdown.Option("MATRIMONIAL"),
                            ])  
    habpis = TextField(label="Piso Habitación",width=400)
    habnum = TextField(label="Número Habitación",width=400)

    #Vista Cliente
    ructxt = TextField(label="RUC", disabled=True)
    empnomtxt = TextField(label="Nombre Empresa", disabled=True)
    razsoctxt = TextField(label="Razón Social", disabled=True)

    #Cositas
    def radiogroup_changed(e):
        if e.control.value == 'EMPRESA':
            ructxt.disabled = False
            empnomtxt.disabled = False
            razsoctxt.disabled = False
        
        elif e.control.value == 'NORMAL':
            ructxt.disabled = True
            empnomtxt.disabled = True
            razsoctxt.disabled = True
        page.update()

    page.update()

    #Escoger Empresa o Normal
    cg = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="NORMAL", label="NORMAL"),
        ft.Radio(value="EMPRESA", label="EMPRESA")
    ]),
    on_change=radiogroup_changed)

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
    
    #Agregar datos boton
    def addtodb(e):
        try:
            pass
            #Limpiar columnas
            mydt.rows.clear()
            # load_data()
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
            # load_data()
            page.snack_bar = SnackBar(
                    Text("Registro Cancelado", size=15),
                    bgcolor="yellow",
                )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print("Error en el código")
    
    #Agregar a la página 
    content = ft.Column([
        ft.Row([
            ft.Text("HACER RESERVA", size=30)
        ],
        alignment=ft.MainAxisAlignment.CENTER),

        ft.Column([
            ft.Row([
                ft.Column([
                    ft.Text("ADMINISTRADOR"),
                    ft.Row([
                        admcod,
                    ]),
               ]),
               ft.Column([
                    ft.Text("FECHA ENTRADA"),
                    ft.Row([
                        fecentaño,
                        fecentmes,
                        fecentdia,
                    ])
                ]),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ]),

        ft.Column([
            ft.Row([
                ft.Column([ 
                    ft.Text("DATOS HUESPED:"),
                    huecod, dni, apepat, apemat, nom, tel
                ]),
                ft.Column([
                    ft.Text("DATOS HABITACIÓN:"),
                    habcatcod,habcod, habpis, habnum
                ])
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND)
        ]),

        ft.Column([
            ft.Row([
                ft.Column([
                    ft.Text("CLIENTE"),
                    ft.Column([
                        cg,ructxt,empnomtxt, razsoctxt
                    ])
                ]),
                ft.Column([
                    ft.Text("ESTADO RESERVA"),
                    ft.Row([
                        resest
                    ])
                ]),
                ft.Column([
                    ft.Text("FECHA SALIDA"),
                    ft.Row([
                        fecsalaño,
                        fecsalmes,
                        fecsaldia,
                    ])
                ]),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ]),

        ft.Column([
            ft.Row([
                ft.Column([
                    ft.Row([
                        ElevatedButton("AGREGAR", on_click=addtodb, bgcolor=ft.colors.TEAL, height=50, color=ft.colors.BLACK),
                        ElevatedButton("CANCELAR", on_click=cancelIn, bgcolor=ft.colors.RED, height=50, color=ft.colors.BLACK),
                    ])
                ]),
            ],
            alignment=ft.MainAxisAlignment.CENTER),
        ]),
    ])
    
    return content
