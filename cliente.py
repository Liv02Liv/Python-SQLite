import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
                id_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Cidade TEXT NOT NULL,
                Idade INT 
                )""")

cursor.execute("""
INSERT INTO cliente
                (Nome, Cidade, Idade) 
VALUES
                ("Ana Souza", "São Paulo", 28),
                ("Carlos Lima", "Curitiba", 35),
                ("Fernada Alves", "São Paulo", 24),
                ("Marcos Silva", "Recife", 41),
                ("Juliana Rocha", "Curitiba", 31)
                """)

conexao.commit()