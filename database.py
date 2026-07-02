import sqlite3


def criar_db():
    connection = sqlite3.connect("estoque.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            nome TEXT NOT NULL,
            ref INTEGER NOT NULL UNIQUE,
            quantidade INTEGER NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def criar_produtos(nome, referencia, quantidade):
    connection = sqlite3.connect("estoque.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, ref, quantidade) VALUES (?, ?, ?)", (nome, referencia, quantidade)
    )

    connection.commit()
    connection.close()

def listar_produtos():
    connection = sqlite3.connect("estoque.db")
    cursor = connection.cursor()

    connection = sqlite3.connect("estoque.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    connection.close()

    return produtos
       
def excluir_produto(ref):
    connection = sqlite3.connect("estoque.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM produtos WHERE ref = ?", 
    (ref,)
    )

    connection.commit()
    connection.close()

def qntd_increase(ref):
    connection = sqlite3.connect("estoque.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE produtos
        SET quantidade = quantidade + 1
        WHERE ref = ?
        """,
        (ref,)
    )

    connection.commit()
    connection.close()
