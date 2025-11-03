from Model.Medico import Medico
from Model.Paciente import Paciente
from Model.Administrador import Admnistrador
from Model.Gestor import Gestor
from database.connection import DbConnection

class Gestao:
    def __init__(self):
        self.db = DbConnection()

    def entrar(self):
        print("\n=== SGHSS Admin ===")
        usuario_login = input("Usuário: ")
        senha_login = input("Senha: ")
         
        admin = Admnistrador.login_admin()

        if (usuario_login == admin.email) & (senha_login == admin.senha):
            print("Login realizado com sucesso.")
            self.menu()
        else:
            print("\nUsuário ou senha incorretos")

    def menu(self):
        while True:
                print("\n=== SISTEMA DE GESTÃO HOSPITALAR ===")    
                print("\nEscolha a sessão:")
                print("1. Gestores")        
                print("2. Médicos")
                print("3. Pacientes")
                print("4. Sair")

                opcao = input("Escolha uma categoria: ")

                if opcao == "1":
                    print("\nBem vindo à categoria de gestores.")
                    print("1. Adicionar gestor")
                    print("2. Listar gestores")
                    print("3. Sair")

                    opcao_gestor = input("Escolha a sua opção: ")
                    if opcao_gestor == "1":
                        self.adicionar_gestor()
                    elif opcao_gestor == "2":
                        Gestor.listar(self.db)
                    elif opcao_gestor == "3":
                        print("\nEncerrando o sistema...")
                        self.db.close()
                        break
                    else:
                        print("\nOpção inválida!")

                elif opcao == "2":
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
                
                elif opcao == "3":
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
               
                elif opcao == "4":
                        print("\nEncerrando o sistema...")
                        break
                else:
                    print("\nOpção inválida!")

    def adicionar_gestor(self):
        nome = input("Nome completo: ")
        cpf = int(input("CRM: "))
        cargo = input("Cargo: ")
        email = input("E-mail: ")
        senha = input("Senha: ")

        gestor = Gestor(nome, cpf, cargo, email, senha)
        gestor.cadastrar_gestor(self.db)
        print(f"\nGestor {gestor.nome} cadastrado com sucesso!")

    def adicionar_paciente(self):
        nome = input("Nome completo: ")
        idade = int(input("Idade: "))
        email = input("E-mail: ")

        paciente = Paciente(nome, idade, email)
        paciente.cadastrar_paciente(self.db)
        print(f"\n Paciente {paciente.nome} cadastrado com sucesso!")

    def adicionar_medico(self):
        nome = input("Nome completo: ")
        crm = int(input("CRM: "))
        email = input("E-mail: ")

        medico = Medico(nome, crm, email)
        medico.cadastrar_medico(self.db)
        print(f"\n Médico {medico.nome} cadastrado com sucesso!")

            
