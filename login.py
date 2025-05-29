import flet as ft
from ui.botoes import criar_botao, criar_campo
from database import verificar_login, carregar_progresso

def login(page: ft.Page, on_navigate):
    page.controls.clear()
    
    # Campos estilizados
    campo_login = criar_campo("Login")
    campo_senha = criar_campo("Senha", senha=True)
    mensagem = ft.Container(
        content=ft.Text(
            "", 
            color="yellow", 
            size=20, 
            weight=ft.FontWeight.BOLD
        ),
        bgcolor="rgba(0, 0, 0, 0.5)",
        border_radius=10,
        padding=10
    )
   
    def pegar_valor_campo(campo: ft.Stack) -> str:
        return campo.controls[1].content.value.strip()

    def tentar_login(e):
        login_valor = pegar_valor_campo(campo_login)
        senha_valor = pegar_valor_campo(campo_senha)

        if not login_valor or not senha_valor:
            mensagem.content.value = "Preencha todos os campos."
        elif verificar_login(login_valor, senha_valor):
            mensagem.content.value = ""

            # Carrega progresso do usuário
            progresso = carregar_progresso(login_valor)
            if progresso is None:
                progresso = {
                    "nome_personagem": "NovoHerói",
                    "classe": "Guerreiro",
                    "nivel": 1,
                    "forca": 5,
                    "inteligencia": 3,
                    "agilidade": 4,
                }
            page.session.set("login_usuario", login_valor)
            page.session.set("progresso", progresso)
            on_navigate("menu")
        else:
            mensagem.content.value = "Login ou senha incorretos."

        page.update()
   
    # Botões estilizados
    botao_entrar = criar_botao("Entrar", tentar_login)
    botao_cadastrar = criar_botao("Cadastrar", lambda e: on_navigate("cadastro"))
    botao_sair = criar_botao("Sair", lambda e: on_navigate("sair"))

    login_column = ft.Column(
        controls=[
            campo_login,
            campo_senha,
            mensagem,
            botao_entrar,
            botao_cadastrar,
            botao_sair
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    overlay = ft.Container(
        content=login_column,
        alignment=ft.alignment.center,
        expand=True,
    )

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

    page.add(ft.Stack(
        controls=[
            fundo,
            overlay,
        ],
        expand=True
    ))
