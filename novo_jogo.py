import flet as ft
from ui.botoes import criar_botao, criar_campo
from ui.custom_char import barra_status, pele_personagem, seletor_vocacao, seletor_cabelo
from database import salvar_progresso, carregar_progresso

def novo_jogo(page: ft.Page, on_navigate):
    page.controls.clear()
    page.title = "Meu Jogo RPG"
    page.window.width = 700
    page.window.height = 900
    page.window.resizable = False
    page.bgcolor = "black"
    page.padding = 0
    page.spacing = 0

    largura_bg = 700
    altura_bg = 900

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

    forca_barra, forca_ref = barra_status(
        imagem_nome="assets/menu/btn_for.png",
        imagem_status_on="assets/menu/atributo_on.png",
        valor_inicial=3,
        page=page
    )

    magic_barra, magic_ref = barra_status(
        imagem_nome="assets/menu/btn_magic.png", 
        imagem_status_on="assets/menu/atributo_on.png",
        valor_inicial=3,
        page=page
    )

    vida_barra, vida_ref = barra_status(
        imagem_nome="assets/menu/btn_life.png", 
        imagem_status_on="assets/menu/atributo_on.png",
        valor_inicial=3,
        page=page
    )

    mana_barra, mana_ref = barra_status(
        imagem_nome="assets/menu/btn_mana.png", 
        imagem_status_on="assets/menu/atributo_on.png",
        valor_inicial=3,
        page=page
    )
    
    imagem_vocacao_ref = ft.Ref[ft.Image]()
    
    imagem_vocacao_control, seletor = seletor_vocacao(
        page,
        imagem_vocacao_ref=imagem_vocacao_ref,
        largura=300,
        altura=180
    )
    
    imagem_cabelo_control, selec_cabelo = seletor_cabelo(page, largura=300, altura=180)

    login = page.client_storage.get("login_usuario")
    if login:
        dados = carregar_progresso(login)
    else:
        dados = None

    valor_opacidade_pele = 4  # default
    if dados and "imagem_pele_opacidade" in dados:
        valor_opacidade_pele = dados["imagem_pele_opacidade"]
    customizador_container, imagem_pele_control = pele_personagem(
        imagem_base="assets/menu/char_base.png",
        imagem_sobreposta="assets/menu/char_base2.png",
        imagem_vocacao=imagem_vocacao_control,
        imagem_cabelo=imagem_cabelo_control,
        valor_inicial=valor_opacidade_pele,
        largura=300,
        altura=180,
        page=page
    )
    
    def salvar_dados(e):
        login = page.client_storage.get("login_usuario")

        if not login:
            print("Usuário não está logado.")
            return

        # Extrai a classe a partir do nome do arquivo da imagem de vocação
        classe = imagem_vocacao_ref.current.src.split("/")[-1].split(".")[0].capitalize()

        salvar_progresso(
            login=login,
            nome_personagem="Heroi",
            classe=classe,
            forca=int(forca_ref.current.value),
            magic=int(magic_ref.current.value),
            vida=int(vida_ref.current.value),
            mana=int(mana_ref.current.value),
            imagem_base="assets/menu/char_base.png",
            imagem_vocacao=imagem_vocacao_ref.current.src,
            imagem_cabelo=imagem_cabelo_control.src,
            imagem_pele_opacidade=imagem_pele_control.opacity
        )

        print("Dados salvos com sucesso!")
        on_navigate("menu")

    voltar = criar_botao("Voltar", lambda e: on_navigate("menu"))
    salvar = criar_botao("Salvar", salvar_dados)    

    page.add(
       ft.Container(
           content=customizador_container,
           width=1,
           height=1
       )
   )
    
    page.add(
        ft.Stack(
            expand=True,
            controls=[
                fundo,
                ft.Column(
                    controls=[
                        ft.Container(height=page.height * 0.1),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Container(
                                    width=300,
                                    height=200,
                                    alignment=ft.alignment.center,
                                    content=ft.Stack(
                                        alignment=ft.alignment.center,
                                        controls=[
                                            ft.Image(
                                                src="assets/menu/fundo_menu.png",
                                                width=300,
                                                height=200,
                                                fit=ft.ImageFit.COVER
                                            ),
                                            ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                expand=True,
                                                controls=[
                                                    customizador_container,  # corrigido aqui
                                                ]
                                            )
                                        ]
                                    )
                                ),

                                ft.Container(
                                    width=300,
                                    height=200,
                                    alignment=ft.alignment.center,
                                    content=ft.Stack(
                                        alignment=ft.alignment.center,
                                        controls=[
                                            ft.Image(
                                                src="assets/menu/fundo_menu.png",
                                                width=300,
                                                height=200,
                                                fit=ft.ImageFit.COVER
                                            ),
                                            ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                expand=True,
                                                controls=[
                                                    forca_barra,
                                                    magic_barra,
                                                    vida_barra,
                                                    mana_barra,
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),

                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Container(
                                    width=300,
                                    height=200,
                                    alignment=ft.alignment.center,
                                    content=ft.Stack(
                                        alignment=ft.alignment.center,
                                        controls=[
                                            ft.Image(
                                                src="assets/menu/fundo_menu.png",
                                                width=300,
                                                height=200,
                                                fit=ft.ImageFit.COVER
                                            ),
                                            ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                expand=True,
                                                controls=[
                                                    seletor
                                                ]
                                            )
                                        ]
                                    )
                                ),

                                ft.Container(
                                    width=300,
                                    height=200,
                                    alignment=ft.alignment.center,
                                    content=ft.Stack(
                                        alignment=ft.alignment.center,
                                        controls=[
                                            ft.Image(
                                                src="assets/menu/fundo_menu.png",
                                                width=300,
                                                height=200,
                                                fit=ft.ImageFit.COVER
                                            ),
                                            ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                expand=True,
                                                controls=[
                                                    selec_cabelo
                                                ]
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),

                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                voltar,
                                salvar
                            ]
                        )
                    ]
                ),
            ]
        ),
    )





