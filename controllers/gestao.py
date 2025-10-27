from Model.Medico import Medico
from Model.Paciente import Paciente
from database.connection import DbConnection

class Gestao:
    def __init__(self):
        self.db = DbConnection()

    def menu(self):
        while True:
                print("\n=== SISTEMA DE GESTÃO HOSPITALAR ===")    
                print("1. Médicos")
                print("2. Pacientes")
                print("3. Sair")

                opcao = input("Escolha uma categoria: ")

                if opcao == "1":
                    print("Bem vindo à categoria de médicos.")
                    print("1. Adicionar médico")
                    print("2. Listar médicos")
                    print("3. Sair")

                    opcao_medico = input("Escolha a sua opção: ")
                    if opcao_medico == "1":
                        self.adicionar_medico()
                    elif opcao_medico == "2":
                        Medico.listar(self.db)
                    elif opcao_medico == "3":
                        print("\nEncerrando o sistema...")
                        self.db.close()
                        break
                    else:
                        print("\nOpção inválida!")
                
                elif opcao == "2":
                    print("Bem vindo à categoria de pacientes.")
                    print("1. Adicionar paciente")
                    print("2. Listar pacientes")
                    print("3. Sair")
                    
                    opcao_paciente = input("Escolha uma opção: ")

                    if opcao_paciente == "1":
                        self.adicionar_paciente()
                    elif opcao_paciente == "2":
                        Paciente.listar(self.db)
                    elif opcao_paciente == "3":
                        print("\nEncerrando o sistema...")
                        self.db.close()
                        break
                    else:
                        print("\nOpção inválida!")
               
                elif opcao == "3":
                        print("\nEncerrando o sistema...")
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

    def adicionar_medico(self):
        nome = input("Nome completo: ")
        crm = int(input("CRM: "))
        email = input("E-mail: ")

        medico = Medico(nome, crm, email)
        medico.cadastrar(self.db)
        print(f"\n Médico {medico.nome} cadastrado com sucesso!")

            
