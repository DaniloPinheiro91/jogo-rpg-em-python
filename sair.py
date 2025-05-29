import flet as ft

def sair(page: ft.Page):
    page.controls.clear()
    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Container(
                width=566,
                height=838,
                alignment=ft.alignment.center,
                content=ft.Stack(
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src="assets/menu/bg.png",
                                width=566,
                                height=838,
                                fit=ft.ImageFit.NONE,
                            ),
                            alignment=ft.alignment.center,
                            expand=True,
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Image(
                                src="assets/menu/fundo_menu.png",
                                width=350,
                                height=200,
                                fit=ft.ImageFit.COVER,
                            ),
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Text(
                                "Obrigado por jogar! \n Você pode fechar a janela.",
                                color="black",
                                weight=ft.FontWeight.BOLD,
                                size=25,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ),
                    ],
                    expand=True,
                    alignment=ft.alignment.center,
                ),
            ),
        )
    )

