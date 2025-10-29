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