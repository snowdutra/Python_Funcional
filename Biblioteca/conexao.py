import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port='700',
        database='Biblioteca'
    )

print("Conexão com o banco de dados estabelecida com sucesso.")