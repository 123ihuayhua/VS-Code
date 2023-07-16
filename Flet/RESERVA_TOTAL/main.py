import flet as ft

from FletRouter import Router
from app_bar import NavBar

def main(page: ft.Page):

    page.theme_mode = "dark"

    page.appbar = NavBar(page)
    myRouter = Router(page)

    page.on_route_change = myRouter.route_change
    page.window_maximized = True
    page.update()
    page.add(
        myRouter.body
    )

    page.go('/')


ft.app(target=main, assets_dir="assets")