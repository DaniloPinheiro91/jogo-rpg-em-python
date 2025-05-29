import flet as ft
from ui.botoes import criar_botao, criar_campo
from database import usuario_existe, cadastrar_usuario
from seguranca import hash_senha, verificar_senha
import re

def cadastro(page: ft.Page, on_navigate):
    page.controls.clear()

    campo_login = criar_campo("Login")
    campo_senha = criar_campo("Senha", senha=True)
    campo_confirma = criar_campo("Confirmar Senha", senha=True)

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

    def senha_forte(senha: str) -> bool:
        if len(senha) < 8:
            return False
        if not re.search(r"[A-Z]", senha):  # letra maiúscula
            return False
        if not re.search(r"[a-z]", senha):  # letra minúscula
            return False
        if not re.search(r"[0-9]", senha):  # número
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):  # caractere especial
            return False
        return True
    
    def pegar_valor_campo(campo: ft.Stack) -> str:
        return campo.controls[1].content.value.strip()
    
    def registrar(e):
        login = campo_login.controls[1].content.value.strip()
        senha = campo_senha.controls[1].content.value.strip()
        confirmar = pegar_valor_campo(campo_confirma)
        MIN_LOGIN = 5

        if not login or not senha or not confirmar:
            mensagem.content.value = "Preencha todos os campos."
        elif len(login) < MIN_LOGIN:
            mensagem.content.value = f"O login deve ter no mínimo {MIN_LOGIN} caracteres."
        elif not senha_forte(senha):
            mensagem.content.value = (
                "A senha deve ter no mínimo 8 caracteres, com letras \nmaiúscula, "
                "minúscula, número e símbolo."
            )
        elif senha != confirmar:
            mensagem.content.value = "As senhas não coincidem."
        elif usuario_existe(login):
            mensagem.content.value = "Usuário já existe."
        else:
            senha_hash = hash_senha(senha)
            if cadastrar_usuario(login, senha_hash):
                mensagem.content.value = "Cadastro realizado com sucesso!"
                mensagem.content.color = "green"
            else:
                mensagem.content.value = "Erro ao cadastrar usuário."

        page.update()

    conteudo = ft.Column(
        controls=[
            campo_login,
            campo_senha,
            campo_confirma,
            mensagem,
            criar_botao("Registrar", registrar),
            criar_botao("Voltar", lambda e: on_navigate("login"))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    page.add(
        ft.Stack(
            expand=True,
            alignment=ft.alignment.center,
            controls=[
                ft.Container(
                    width=566,
                    height=838,
                    content=ft.Image(
                        src="assets/menu/bg.png",
                        width=566,
                        height=838,
                        fit=ft.ImageFit.FILL,
                    ),
                ),
                ft.Container(
                    content=conteudo,
                    alignment=ft.alignment.center,
                ),
            ],
        )
    )

