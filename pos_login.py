import flet as ft
from ui.botoes import criar_botao, criar_selecao
from database import carregar_progresso

def pos_login(page: ft.Page, on_navigate):
    page.controls.clear()

    largura_bg = 566
    altura_bg = 838
    
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
    
    fundo_novo_jogo = ft.Container(
        padding=ft.Padding(0, 0, 0, 30),
        content=ft.Image(
            src="assets/menu/fundo_menu.png",
            width=450,
            height=225,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center,
    )

    login_usuario = page.client_storage.get("login_usuario")
    progresso = None

    if login_usuario:
        progresso = carregar_progresso(login_usuario)
        if progresso:
            page.client_storage.set("progresso", progresso)
            
    def clique_novo_jogo(e):
        on_navigate("novo_jogo")

    def clique_continuar(e):
        login_usuario = page.client_storage.get("login_usuario")

        if not login_usuario:
            page.snack_bar = ft.SnackBar(ft.Text("Erro: nenhum usuário logado."))
            page.snack_bar.open = True
            page.update()
            return

        progresso = page.client_storage.get("progresso")

        if not progresso:
            progresso = carregar_progresso(login_usuario)

        if not progresso:
            page.snack_bar = ft.SnackBar(ft.Text("Erro: nenhum progresso salvo encontrado."))
            page.snack_bar.open = True
            page.update()
            return

        mensagem = (
            f"Carregando jogo de {progresso['nome_personagem']} (Classe: {progresso['classe']}, "
            f"Nível: {progresso['nivel']})"
        )
        page.snack_bar = ft.SnackBar(ft.Text(mensagem))
        page.snack_bar.open = True
        page.update()
        page.client_storage.set("progresso", progresso)
        on_navigate("jogo")
        
    botao_1 = criar_selecao("Continuar", "btn_continue.png", clique_continuar)
    botao_2 = criar_selecao("Novo Jogo", "btn_novo.png", clique_novo_jogo)
    voltar = criar_botao("Voltar", lambda e: on_navigate("login"))

    conteudo = ft.Column(
        controls=[
            ft.Text("Bem-vindo de volta!", size=24, weight=ft.FontWeight.BOLD, color="white"),
            botao_1,
            botao_2,
            voltar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    overlay = ft.Container(
        content=conteudo,
        alignment=ft.alignment.center,
        expand=True,
    )

    page.add(
        ft.Stack(
            controls=[fundo, fundo_novo_jogo, overlay],
            expand=True
        )
    )
    page.update()


