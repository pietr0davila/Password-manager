from Databases import Databases
from .utils import account_menu, encrypt_hash
from getpass import getpass

def login():
    db = Databases(db_name="databases/users.db", table="users")
    while True:
        # Loop para solicitar usuário e senha
        # INPUTS PARA VERSÃO FINAL
        username = input("Digite o seu nome de usuário: ").strip()
        user_pass = getpass("Digite sua senha (echo no terminal desabilitado!)").strip()
        success, result = db.get_users(username, user_pass)
        if not success:
            if result == "invalid_pass":
                print("[-] Sentimos muito, sua senha é inválida, tente novamente")
                return False, False
            elif result == "non_existent_user":
                print("[-] Não conseguimos encontrar seu usuário, tente criar um!")
                account_menu()
                return False, False
        else:
            username = success
            user_id = result
            # Corrigir
            print("[+] Você foi autenticado com sucesso!", username)
            return user_id, username
