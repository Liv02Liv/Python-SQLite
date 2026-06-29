import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                valor FLOAT
                )""")

cursor.execute("""
INSERT INTO pedidos
                (nome, valor) 
VALUES
                ("Carlos", 85.99),
                ("Roberta", 52.45),
                ("Leticia", NULL),
                ("Joao", NULL),
                ("Luis", NULL),
                ("Davy", 220.22),
                ("Bruna", 345.49),
                ("Lucas", 271.35)
                """)

conexao.commit()