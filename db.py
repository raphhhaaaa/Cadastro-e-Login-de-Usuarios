import sqlite3

DB_NAME = 'usuarios.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   usuario VARCHAR(20) NOT NULL,
                   nascimento YEAR,
                   sexo CHAR(1) CHECK(sexo IN ('M', 'F')),
                   nacionalidade VARCHAR(10) DEFAULT 'Brasil',
                   hash TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def cadastro_usuario(usuario, nascimento, sexo, nacionalidade, hash):
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, nascimento, sexo, nacionalidade, hash) VALUES (?, ?, ?, ?, ?)", (usuario, nascimento, sexo, nacionalidade, hash,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print('=-' * 25)
        print(f'Ocorreu um erro ao inserir dados: {e}')
        print('=-' * 25)
        return False
    finally:
        if conn:    
            conn.close()

def mostrar_usuarios():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def apagar_usuario(id):
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print('=-' * 25)
        print(f'Houve um erro ao apagar dados: {e}')
        print('=-' * 25)
        return False
    finally:
        if conn:
            conn.close()

def pega_hashsenha(usuario):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT hash FROM usuarios WHERE usuario = ?", (usuario,))
    senha = cursor.fetchall()
    conn.close()
    for s in senha:
        senha = s[0]
    return senha

def atualiza_dados(campo, novo_valor, id):
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE usuarios SET {campo} = ? WHERE id = ?", (novo_valor, id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print('=-' * 25)
        print(f'Erro ao atualizar dados: {e}')
        print('=-' * 25)
        return False
    finally:
        if conn:
            conn.close()

def mostra_ids():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuarios")
    ids = cursor.fetchall()
    conn.close()
    lista_ids = []
    for i in ids:
        lista_ids.append(i[0])
    return lista_ids