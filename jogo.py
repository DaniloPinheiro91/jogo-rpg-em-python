import flet as ft
from ui.botoes import criar_botao

def tela_jogo(page: ft.Page, on_navigate):
    
    largura_bg = 566
    altura_bg = 838
    
    fundo_novo_jogo = ft.Container(
        padding=ft.Padding(0, 0, 0, 30),
        content=ft.Image(
            src="assets/menu/fundo_menu.png",
            width=550,
            height=300,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center,
    )
    
    fundo = ft.Container(
        content=ft.Image(
            src="assets/menu/bg.png",
            width=largura_bg,
            height=altura_bg,
            fit=ft.ImageFit.NONE,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )
    
    
    progresso = page.client_storage.get("progresso")

    if not progresso:
        page.snack_bar = ft.SnackBar(ft.Text("Erro: progresso não carregado."))
        page.snack_bar.open = True
        page.update()
        return

    imagem_base = progresso.get("imagem_base", "assets/menu/char_base.png")
    imagem_vocacao = progresso.get("imagem_vocacao", "assets/menu/default_vocacao.png")
    imagem_cabelo = progresso.get("imagem_cabelo", "assets/menu/default_cabelo.png")
    imagem_pele_opacidade = progresso.get("imagem_pele_opacidade", 1.0)
    
    imagem_pele = ft.Image(
        src="assets/menu/char_base2.png",
        width=300,
        height=180,
        opacity=imagem_pele_opacidade
)

    
    # Monta a imagem do personagem com camadas
    personagem = ft.Stack(
        width=300,
        height=180,
        controls=[
            ft.Image(src=imagem_base, width=300, height=180),
            imagem_pele,
            ft.Image(src=imagem_vocacao, width=300, height=180),
            ft.Image(src=imagem_cabelo, width=300, height=180),
        ]
    )

    # Botão para voltar ao menu principal
    voltar = criar_botao("Voltar", lambda e: on_navigate("menu"))


    page.controls.clear()
    
    # adiciona todo o conteudo na tela
    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Stack(
                controls=[
                    fundo,
                    fundo_novo_jogo,
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=30,
                            controls=[
                                ft.Container(height=80),
                                ft.Text(
                                    f"{progresso['nome_personagem']} - {progresso['classe']}",
                                    size=30,
                                    weight="bold"
                                ),
                                personagem,  
                                voltar
                            ]
                        )
                    )
                ],
                expand=True
            )
        )
    )
    page.update()