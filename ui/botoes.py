import flet as ft

def criar_botao(texto: str, ao_clicar, largura=250, altura=80, cor_texto="black"):
    return ft.GestureDetector(
        on_tap=ao_clicar,
        content=ft.Container(
            width=largura,
            height=altura,
            content=ft.Stack(
                controls=[
                    ft.Image(
                        src="assets/menu/botao.png",
                        width=largura,
                        height=altura,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Container(
                        content=ft.Text(
                            texto,
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=cor_texto,
                            text_align=ft.TextAlign.CENTER
                        ),
                        alignment=ft.alignment.center,
                        width=largura,
                        height=altura
                    )
                ]
            )
        )
    )


def criar_campo(rotulo: str, senha: bool = False) -> ft.Stack:
    largura = 300
    altura = 90

    return ft.Stack(
        width=largura,
        height=altura,
        controls=[
            ft.Image(
                src="assets/menu/fundo_menu.png",
                width=largura,
                height=altura,
                fit=ft.ImageFit.FILL
            ),
            ft.Container(
                alignment=ft.alignment.center,
                padding=ft.padding.only(left=10, right=10),
                content=ft.TextField(
                    label=rotulo,
                    password=senha,
                    can_reveal_password=senha,
                    border_color="transparent",
                    color="black",
                    label_style=ft.TextStyle(color="black"),
                    bgcolor="transparent",
                    text_align=ft.TextAlign.LEFT,
                    width=360,
                    height=altura - 20
                )
            )
        ]
    )

# Função que cria o botão estilizado para seleção de jogo
def criar_selecao(texto: str, imagem_btn: str, ao_clicar, largura=250, altura=80, cor_texto="black"):
    return ft.GestureDetector(
        on_tap=ao_clicar,
        content=ft.Container(
            width=largura,
            height=altura,
            content=ft.Stack(
                controls=[
                # Fundo
                    ft.Image(
                        src="assets/menu/fundo_transp.png",
                        width=largura,
                        height=altura,
                        fit=ft.ImageFit.FILL
                    ),
                    # Conteúdo: imagem a esquerda e texto a direita
                    ft.Container(
                        width=largura,
                        height=altura,
                        padding=ft.Padding(5, 0, 0, 0),
                        alignment=ft.alignment.center,
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src=f"assets/menu/{imagem_btn}",
                                    width=50,
                                    height=50,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.Container(
                                    padding=ft.Padding(0, 0, 40, 0),
                                    content=ft.Text(
                                        texto,
                                        size=22,
                                        weight=ft.FontWeight.BOLD,
                                        color=cor_texto
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    )
                ]
            )
        )
    )