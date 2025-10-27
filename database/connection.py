import mysql.connector

class DbConnection:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="sghss"
        )
        self.cursor = self.conexao.cursor()

    def commit(self):
        self.conexao.commit()

    def close(self):
        self.cursor.close()
        self.conexao.close()
