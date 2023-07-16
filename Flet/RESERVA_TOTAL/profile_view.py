import flet as ft
from index_view import *
import mysql.connector

# Conexión BD
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    port=3306,
    password='12345',  # contraseña
    database='HOTEL'
)
cursor = mydb.cursor()


def ProfileView(page):
    content = ft.Column([
        ft.Row([
            
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
    ])

    return content
