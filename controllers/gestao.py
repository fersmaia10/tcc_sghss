from Model.Paciente import Paciente
from database.connection import DbConnection

class Gestao:
    def __init__(self):
        self.db = DbConnection()

    def menu(self):
        while True:
            print("\n=== SISTEMA DE GESTÃO HOSPITALAR ===")
            print("1. Adicionar paciente")
            print("2. Listar pacientes")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_paciente()
            elif opcao == "2":
                Paciente.listar(self.db)
            elif opcao == "3":
                print("\nEncerrando o sistema...")
                self.db.close()
                break
            else:
                print("\nOpção inválida!")

    def adicionar_paciente(self):
        nome = input("Nome completo: ")
        idade = int(input("Idade: "))
        email = input("E-mail: ")

        paciente = Paciente(nome, idade, email)
        paciente.cadastrar(self.db)
        print(f"\n Paciente {paciente.nome} cadastrado com sucesso!")
