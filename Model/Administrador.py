from Model.Gestor import Gestor
from Model.Medico import Medico
from Model.Paciente import Paciente

class Admnistrador:
    def __init__(self, nome, cpf, email, cargo, senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cargo = cargo
        self.senha = senha

    def login_admin():
        return Admnistrador(
            nome = "Admin",
            cpf = "00000000000",
            email = "admin",
            cargo = "RH",
            senha = "admin")
    
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