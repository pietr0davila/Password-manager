import time
from Databases import Databases
from accounts_treat.utils import decrypt_pass
db = Databases(db_name="databases/manager.db", table="manage_passwords")

def init_database():
    db.setup_password_db()

def list_password(user_id):
    init_database()
    try:
        returned_values = db.list_passwords(user_id)
        if not returned_values: 
            print("[-] Você não tem senhas armazenadas!")
        else:  
            for service, username, password in returned_values:
                decrypt_pass(password)
                print(f"[+] Serviço: {service}\n")
                print(f"[+] Nome de usuário: {username}\n")
                print(f"[+] Senha: {password}\n")
                print("-" * 20)
        time.sleep(5)

    except Exception as e:
        print("[-] Houve um erro ao tentar listar suas senhas", e)