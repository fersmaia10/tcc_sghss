class Paciente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def cadastrar(self, db):
        sql = "INSERT INTO paciente (nome, idade, email) VALUES (%s, %s, %s)"
        valores = (self.nome, self.idade, self.email)
        db.cursor.execute(sql, valores)
        db.commit()

    @staticmethod
    def listar(db):
        db.cursor.execute("SELECT * FROM paciente")
        resultados = db.cursor.fetchall()
        
        if not resultados:
            print("\nNenhum paciente cadastrado.")
        else:
            print("\n--- Lista de Pacientes ---")
            for pacientes in resultados:
                print(f"ID: {pacientes[0]} | Nome: {pacientes[1]} | Idade: {pacientes[2]} | E-mail: {pacientes[3]}")