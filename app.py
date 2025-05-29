import flet as ft
from login import login
from cadastro import cadastro
from sair import sair
from database import criar_banco
from pos_login import pos_login
from novo_jogo import novo_jogo
from jogo import tela_jogo

def main(page: ft.Page):
    criar_banco()
    page.title = "Meu Jogo RPG"
    page.window.width = 700
    page.window.height = 860
    page.window.resizable = False
    page.bgcolor = "black"
    page.padding = 0
    page.spacing = 0

    def navegar(tela):
        page.controls.clear()
        if tela == "menu":
            pos_login(page, navegar)
        elif tela == "cadastro":
            cadastro(page, navegar)
        elif tela == "login":
            login(page, navegar)
        elif tela == "novo_jogo":
            novo_jogo(page, navegar)
        elif tela == "jogo":
            tela_jogo(page, navegar)
        elif tela == "sair":
            sair(page)
            
    navegar("login")

ft.app(target=main)



