import flet as ft

def barra_status(imagem_nome: str, imagem_status_on: str, valor_inicial=0,
    largura=250, altura=40, cor_texto="yellow", page=None):

    # Fatores proporcionais
    proporcao_icone = 1    # Imagem principal (nome) ocupa 90% da altura
    proporcao_botao = 0.9    # Botão ocupa 40% da altura
    proporcao_status = 0.9   # Status_on ocupa 60% da altura

    tamanho_icone = int(altura * proporcao_icone)
    tamanho_botao = int(altura * proporcao_botao)
    tamanho_status = int(altura * proporcao_status)

    valor_ref = ft.Ref[ft.Text]()
    
    valor_texto = ft.Text(
        str(valor_inicial),
        size=int(altura * 0.5),
        color=cor_texto,
        width=int(largura * 0.15),
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD,
        ref=valor_ref
    )

    imagem_titulo = ft.Image(
        src=imagem_nome,
        width=int(largura * 0.4),
        height=tamanho_icone,
        fit=ft.ImageFit.CONTAIN
    )

    status_overlay = ft.Row(spacing=2, wrap=False)   

    def atualizar_status_overlay(valor):
        status_overlay.controls = [
            ft.Image(
                src=imagem_status_on,
                width=int(largura * 0.05),
                height=tamanho_status,
                fit=ft.ImageFit.CONTAIN
            )
            for _ in range(valor)
        ]

    def atualizar_valor(e, num: int):
        valor = int(valor_texto.value)
        novo_valor = valor + num
        if 0 <= novo_valor <= 8:
            valor_texto.value = str(novo_valor)
            atualizar_status_overlay(novo_valor)
            if page:
                page.update()

    def criar_botao_imagem(src, num):
        return ft.GestureDetector(
            on_tap=lambda e: atualizar_valor(e, num),
            content=ft.Image(
                src=src,
                width=tamanho_botao,
                height=tamanho_botao,
                fit=ft.ImageFit.CONTAIN
            )
        )

    botao_mais = criar_botao_imagem("assets/menu/btn_seta_dir.png", 1)
    botao_menos = criar_botao_imagem("assets/menu/btn_seta_esq.png", -1)

    atualizar_status_overlay(valor_inicial)

    container = ft.Container(
        width=largura,
        height=altura,
        padding=ft.padding.only(left=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            controls=[
                ft.Container(width=largura * 0.2, alignment=ft.alignment.center, content=imagem_titulo),
                ft.Container(width=largura * 0.1, alignment=ft.alignment.center, content=botao_menos),
                ft.Container(width=largura * 0.1, alignment=ft.alignment.center, content=botao_mais),
                ft.Container(width=largura * 0.1, alignment=ft.alignment.center, content=valor_texto),
                ft.Container(width=largura * 0.5, alignment=ft.alignment.center_left, content=status_overlay),
            ]
        )
    )

    return container, valor_ref
    
def pele_personagem(imagem_base: str, imagem_sobreposta: str, imagem_vocacao: ft.Image, imagem_cabelo: ft.Image, valor_inicial=4, largura=250, altura=80, page=None):

        proporcao_icone = 1
        proporcao_botao = 0.4

        tamanho_icone = int(altura * proporcao_icone)
        tamanho_botao = int(altura * proporcao_botao)

        imagem_base_control = ft.Image(
            src=imagem_base,
            width=int(largura * 0.4),
            height=tamanho_icone,
            fit=ft.ImageFit.CONTAIN
        )

        imagem_sobreposta_control = ft.Image(
            src=imagem_sobreposta,
            width=int(largura * 0.4),
            height=tamanho_icone,
            fit=ft.ImageFit.CONTAIN,
            opacity=valor_inicial / 8
        )

        stack_personagem = ft.Stack(
            width=int(largura * 0.4),
            height=tamanho_icone,
            controls=[
                imagem_base_control,
                imagem_sobreposta_control,
                imagem_cabelo,
                imagem_vocacao
            ]
        )

        # Funções de controle da opacidade
        def atualizar_opacidade(novo_valor):
            imagem_sobreposta_control.opacity = novo_valor / 8
            page.update()

        def alterar_valor(e, incremento):
            novo_valor = min(8, max(0, int(imagem_sobreposta_control.opacity * 8) + incremento))
            atualizar_opacidade(novo_valor)

        def criar_botao_imagem(src, incremento):
            return ft.GestureDetector(
                on_tap=lambda e: alterar_valor(e, incremento),
                content=ft.Image(
                    src=src,
                    width=tamanho_botao,
                    height=tamanho_botao,
                    fit=ft.ImageFit.CONTAIN
                )
            )

        return ft.Container(
            width=largura,
            height=altura,
            alignment=ft.alignment.center,
            content=ft.Stack(
                width=largura,
                height=altura,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                criar_botao_imagem("assets/menu/btn_seta_esq.png", -1),
                                stack_personagem,
                                criar_botao_imagem("assets/menu/btn_seta_dir.png", 1),
                            ]
                        )
                    )
                ]
            )
        ), imagem_sobreposta_control

def seletor_vocacao(page: ft.Page, imagem_vocacao_ref: ft.Ref[ft.Image], largura=250, altura=80):
    vocacoes = [
        "assets/menu/addon_not.png",
        "assets/menu/addon_knight.png",
        "assets/menu/addon_arch.png",
        "assets/menu/addon_carrasco.png"
    ]

    index_vocacao = 0
    proporcao_icone = 1
    proporcao_botao = 0.4

    tamanho_icone = int(altura * proporcao_icone)
    tamanho_botao = int(altura * proporcao_botao)

    imagem_vocacao = ft.Image(
        src=vocacoes[index_vocacao],
        width=int(largura * 0.4),
        height=tamanho_icone,
        fit=ft.ImageFit.CONTAIN,
        ref=imagem_vocacao_ref 
    )

    def atualizar_vocacao(novo_index):
        nonlocal index_vocacao
        index_vocacao = novo_index % len(vocacoes)
        imagem_vocacao_ref.current.src = vocacoes[index_vocacao]
        page.update()

    def criar_botao_imagem(src, direcao):
        return ft.GestureDetector(
            on_tap=lambda e: atualizar_vocacao(index_vocacao + direcao),
            content=ft.Image(
                src=src,
                width=tamanho_botao,
                height=tamanho_botao,
                fit=ft.ImageFit.CONTAIN
            )
        )

    container = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
        controls=[
            criar_botao_imagem("assets/menu/btn_seta_esq.png", -1),
            imagem_vocacao,
            criar_botao_imagem("assets/menu/btn_seta_dir.png", 1),
        ]
    )

    return imagem_vocacao_ref.current, container

def seletor_cabelo(page: ft.Page, largura=250, altura=80):
            cabelo = [
                "assets/menu/addon_not.png",
                "assets/menu/cabelo1_01.png",
                "assets/menu/cabelo1_02.png",
                "assets/menu/cabelo1_03.png",
                "assets/menu/cabelo2_01.png",
                "assets/menu/cabelo2_02.png",
                "assets/menu/cabelo2_03.png"
            ]

            index_cabelo = 0
            proporcao_icone = 1
            proporcao_botao = 0.4

            tamanho_icone = int(altura * proporcao_icone)
            tamanho_botao = int(altura * proporcao_botao)

            imagem_cabelo = ft.Ref[ft.Image]()

            imagem_vocacao = ft.Image(
                src=cabelo[index_cabelo],
                width=int(largura * 0.4),
                height=tamanho_icone,
                fit=ft.ImageFit.CONTAIN,
                ref=imagem_cabelo
            )

            def atualizar_vocacao(novo_index):
                nonlocal index_cabelo
                index_cabelo = novo_index % len(cabelo)
                imagem_cabelo.current.src = cabelo[index_cabelo]
                page.update()

            def criar_botao_imagem(src, direcao):
                return ft.GestureDetector(
                    on_tap=lambda e: atualizar_vocacao(index_cabelo + direcao),
                    content=ft.Image(
                        src=src,
                        width=tamanho_botao,
                        height=tamanho_botao,
                        fit=ft.ImageFit.CONTAIN
                    )
                )

            container = ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    criar_botao_imagem("assets/menu/btn_seta_esq.png", -1),
                    imagem_vocacao,
                    criar_botao_imagem("assets/menu/btn_seta_dir.png", 1),
                ]
            )

            return imagem_cabelo.current, container


    