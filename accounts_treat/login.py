from Databases import Databases
from .account import account_menu
from getpass import getpass

def login():
    db = Databases(db_name="databases/users.db", table="users")
    while True:
        # Loop para solicitar usuário e senha
        username = input("Digite o seu nome de usuário: ").strip()
        user_pass = getpass("Digite sua senha (echo no terminal desabilitado!)").strip()
        user_exists = db.get_users(username, user_pass)
        print(user_exists)
        
        if user_exists == "invalid_pass":
            print("[-] Sentimos muito, sua senha é inválida, tente novamente")
            return False
        elif user_exists == "non_existent_user":
            print("[-] Não conseguimos encontrar seu usuário, tente criar um!")
            account_menu()
            return False
        else:
            print("[+] Você foi autenticado com sucesso!", username)
            return username
