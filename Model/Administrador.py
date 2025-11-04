from Model.Gestor import Gestor
from Model.Medico import Medico
from Model.Paciente import Paciente

import bcrypt

class Administrador:
    def __init__(self, nome, cpf, email, cargo, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cargo = cargo
        self.senha = senha

    def verificar_login(self, db):
        sql = "SELECT senha FROM administrador WHERE cpf = %s AND senha = %s"
        db.cursor.execute(sql, (self.cpf, self.senha))
        resultado = db.cursor.fetchone()

        if resultado:
            senha_db = resultado[0].encode('utf-8')
            return bcrypt.checkpw(self.senha.encode('utf-8'), senha_db)
        return False
    
    def cadastrar_gestor(self, db):
        sql = "INSERT INTO gestor (nome, cpf, email, senha, cargo) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.nome, self.cpf, self.email, self.senha, self.cargo)
        db.cursor.execute(sql, valores)
        db.commit()

    def cadastrar_medico(self, db):
        sql = "INSERT INTO medico (nome, crm, email) VALUES (%s, %s, %s)"
        valores = (self.nome, self.crm, self.email)
        db.cursor.execute(sql, valores)
        db.commit()

    def cadastrar_paciente(self, db):
        sql = "INSERT INTO paciente (nome, idade, email) VALUES (%s, %s, %s)"
        valores = (self.nome, self.idade, self.email)
        db.cursor.execute(sql, valores)
        db.commit()