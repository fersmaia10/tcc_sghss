class Medico:
    def __init__(self, nome, crm, email):
        self.nome = nome
        self.crm = crm
        self.email = email
        
    def cadastrar(self, db):
        sql = "INSERT INTO medico (nome, crm, email) VALUES (%s, %s, %s)"
        valores = (self.nome, self.crm, self.email)
        db.cursor.execute(sql, valores)
        db.commit()

    @staticmethod
    def listar(db):
        db.cursor.execute("SELECT * FROM medico")
        resultados = db.cursor.fetchall()
        
        if not resultados:
            print("\nNenhum médico cadastrado.")
        else:
            print("\n--- Lista de Médicos ---")
            for medicos in resultados:
                print(f"ID: {medicos[0]} | Nome: {medicos[1]} | CRM: {medicos[2]} | E-mail: {medicos[3]}")