class Medico:
    def __init__(self, nome, crm, email):
        self.nome = nome
        self.crm = crm
        self.email = email

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