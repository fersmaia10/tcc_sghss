from Model import Paciente
from database import DbConnection
from controllers import Gestao


from controllers.gestao import Gestao
if __name__ == "__main__":
    sistema = Gestao()
    sistema.entrar()
