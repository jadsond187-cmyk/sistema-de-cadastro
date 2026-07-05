import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="B.enedeta.105",
    database="sistema_cadastro"
)

cursor = conn.cursor()

def listar():
    cursor.execute("SELECT * FROM pessoas")
    return cursor.fetchall()

def cadastrar(nome, idade, cidade):
    cursor.execute(
        "INSERT INTO pessoas (nome, idade, cidade) VALUES (%s, %s, %s)",
        (nome, idade, cidade)
    )
    conn.commit()

def deletar(id):
    cursor.execute("DELETE FROM pessoas WHERE id=%s", (id,))
    conn.commit()

def editar(id, nome, idade, cidade):
    cursor.execute(
        "UPDATE pessoas SET nome=%s, idade=%s, cidade=%s WHERE id=%s",
        (nome, idade, cidade, id)
    )
    conn.commit()