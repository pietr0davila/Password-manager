from Databases import Databases
from accounts_treat.utils import encrypt_pass
db = Databases(db_name="databases/manager.db", table="manage_passwords")

def init_database():
    db.setup_password_db()


def add_password(user_id):
    init_database()
    try:
        service = input("[+] Serviço (www.google.com): ")
        username = input("[+] Seu nome de usuário: ")
        password = input("[+] Digite sua senha: ")
        crypted_pass = encrypt_pass(password)
        db.add_passwords_to_database(user_id, service, username, crypted_pass)
        print("Adicionado ao Banco de dados")
    except Exception as e:
        print("[-] Erro ao ler os dados", e)
    
    