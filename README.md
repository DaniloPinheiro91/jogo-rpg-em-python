# Projeto Jogo RPG

Um jogo de RPG com customização de personagem, desenvolvido com [Flet](https://flet.dev/) e Python.  
O jogador pode criar seu personagem, definir atributos como força, magia, mana e vida, escolher cabelo e roupas para customizar sua aparência, e salvar seu progresso.

---

## 🚀 Funcionalidades

* Tela de login e cadastro de usuário
* Sistema de criação de personagem com:
  * Seleção de vocação (classe)
  * Escolha de cabelo
  * Controle de atributos (força, magia, vida, mana)
  * Tom de pele ajustável
* Salvamento e carregamento de progresso via banco de dados
* Interface gráfica interativa e personalizada com imagens

---

## 🖼️ Demonstração

* Demonstração via apresentação em PDF

---

## 🛠️ Tecnologias Utilizadas

* [Python](https://www.python.org/) versão: 3.13.2
* [Flet](https://flet.dev/) versão: 0.28.2
* [SQLite](https://www.sqlite.org/index.html) para banco de dados local
* [bcrypt](https://pypi.org/project/bcrypt/) versão: 4.3.0

---

## 📂 Organização do Projeto

/Projeto jogo RPG/
│
├── app.py # Arquivo principal que inicializa a aplicação
├── usuarios.db # Banco de dados SQLite
│
├── cadastro.py # Tela de cadastro de usuários
├── login.py # Tela de login
├── pos_login.py # Tela que aparece após login (ex: menu do jogador)
│
├── jogo.py # Lógica principal do jogo
├── novo_jogo.py # Inicialização de novo jogo
├── sair.py # Tela ou lógica de saída do jogo
│
├── database.py # Funções de acesso/manipulação do banco
├── seguranca.py # Funções de segurança (bcrypt, validações etc.)
├── teste_aplicacao.py # Arquivo de testes manuais ou automatizados
│
├── assets/ # Recursos estáticos (imagens, sons, fontes, etc.)
│ └── menu/ # Imagens do menu do jogo
│
├── ui/ # Componentes visuais/modulares
│ ├── init.py # Torna a pasta um pacote Python
│ ├── botoes.py # Funções para criação de botões estilizados
│ ├── custom_char.py # Interface ou lógica de customização de personagem
│ └── pycache/ # Cache dos arquivos compilados (gerado automaticamente)
│
└── venv/ # Ambiente virtual do projeto (não versionar)

---

## ⚙️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/DaniloPinheiro91/jogo-rpg-em-python.git
cd seu_repositorio
```

2. Crie e ative o ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:

```bash
pip install flet
pip install bcrypt

ou utilize o comando:

pip install -r requirements.txt
```

4. Execute o projeto:

```bash
python app.py
```

---

## 🔒 Segurança

* Senhas dos usuários são armazenadas com hash (usando `hashlib`)
* Validação de campos de login e cadastro com verificação básica

---

## ✍️ Autor

* Danilo Pinheiro – [LinkedIn](https://www.linkedin.com/in/danilo-pinheiro-499592324/) | [GitHub](https://github.com/DaniloPinheiro91)

---

## 📌 Observações

* Projeto desenvolvido como parte do curso Infinity School.
* O banco de dados SQLite está localizado em `usuarios.db`.

---

## 🧹 Melhorias Futuras

* Implementar sistema de batalhas
* Adicionar itens e equipamentos
* Sistema de missões e mapas
