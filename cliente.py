import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
                id_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Cidade TEXT NOT NULL,
                Idade Int
                )""")