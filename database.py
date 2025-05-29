import sqlite3
from seguranca import hash_senha
import bcrypt

# Cria o banco de dados do login e senha dos usuários
def criar_banco():
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()

    # Tabela de usuários
    c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    # Tabela com o "save" do personagem
    c.execute("""
        CREATE TABLE IF NOT EXISTS progresso (
            usuario_id INTEGER PRIMARY KEY,
            nome_personagem TEXT,
            classe TEXT,
            nivel INTEGER DEFAULT 1,
            forca INTEGER DEFAULT 0,
            magic INTEGER DEFAULT 0,
            vida INTEGER DEFAULT 0,
            mana INTEGER DEFAULT 0,
            imagem_base TEXT,
            imagem_vocacao TEXT,
            imagem_cabelo TEXT,
            imagem_pele_opacidade REAL DEFAULT 0,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )
    """)

    c.execute("PRAGMA table_info(progresso)")
    colunas = [col[1] for col in c.fetchall()]
    if "imagem_pele_opacidade" not in colunas:
        c.execute("ALTER TABLE progresso ADD COLUMN imagem_pele_opacidade REAL DEFAULT 0")

    conn.commit()
    conn.close()

def cadastrar_usuario(login: str, senha_hash: str) -> bool:
    try:
        conn = sqlite3.connect("usuarios.db")
        c = conn.cursor()
        c.execute("INSERT INTO usuarios (login, senha) VALUES (?, ?)", (login, senha_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def usuario_existe(login: str) -> bool:
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute("SELECT 1 FROM usuarios WHERE login = ?", (login,))
    resultado = c.fetchone()
    conn.close()
    return resultado is not None

def verificar_login(login, senha_digitada):
    try:
        conn = sqlite3.connect("usuarios.db")
        c = conn.cursor()
        c.execute("SELECT senha FROM usuarios WHERE login = ?", (login,))
        resultado = c.fetchone()
        conn.close()

        if resultado:
            senha_salva_hash = resultado[0]
            return verificar_senha(senha_digitada, senha_salva_hash)
        return False
    except Exception as e:
        print("Erro ao verificar login:", e)
        return False

def verificar_senha(senha_digitada, senha_hash):
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_hash.encode('utf-8'))

def salvar_progresso(login, nome_personagem, classe, forca, magic, vida, mana, 
                     imagem_base, imagem_vocacao, imagem_cabelo, imagem_pele_opacidade, nivel=1):
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()

    c.execute("SELECT id FROM usuarios WHERE login = ?", (login,))
    usuario = c.fetchone()

    if usuario:
        usuario_id = usuario[0]
        c.execute("SELECT 1 FROM progresso WHERE usuario_id = ?", (usuario_id,))
        if c.fetchone():
            c.execute("""
                UPDATE progresso
                SET nome_personagem=?, classe=?, nivel=?, forca=?, magic=?, vida=?, mana=?,
                    imagem_base=?, imagem_vocacao=?, imagem_cabelo=?, imagem_pele_opacidade=?
                WHERE usuario_id=?
            """, (nome_personagem, classe, nivel, forca, magic, vida, mana,
                  imagem_base, imagem_vocacao, imagem_cabelo, imagem_pele_opacidade, usuario_id))
        else:
            c.execute("""
                INSERT INTO progresso (usuario_id, nome_personagem, classe, nivel, forca, magic, vida, mana,
                                       imagem_base, imagem_vocacao, imagem_cabelo, imagem_pele_opacidade)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (usuario_id, nome_personagem, classe, nivel, forca, magic, vida, mana,
                  imagem_base, imagem_vocacao, imagem_cabelo, imagem_pele_opacidade))
        conn.commit()
    conn.close()

def carregar_progresso(login):
    conn = sqlite3.connect("usuarios.db")
    c = conn.cursor()
    c.execute("SELECT id FROM usuarios WHERE login = ?", (login,))
    usuario = c.fetchone()

    if usuario:
        usuario_id = usuario[0]
        c.execute("""SELECT nome_personagem, classe, nivel, forca, magic, vida, mana,
                     imagem_base, imagem_vocacao, imagem_cabelo, imagem_pele_opacidade
                     FROM progresso WHERE usuario_id = ?""", (usuario_id,))
        progresso = c.fetchone()
        conn.close()
        if progresso:
            return {
                "nome_personagem": progresso[0],
                "classe": progresso[1],
                "nivel": progresso[2],
                "forca": progresso[3],
                "magic": progresso[4],
                "vida": progresso[5],
                "mana": progresso[6],
                "imagem_base": progresso[7],
                "imagem_vocacao": progresso[8],
                "imagem_cabelo": progresso[9],
                "imagem_pele_opacidade": progresso[10],
            }
    conn.close()
    return None


