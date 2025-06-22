from Databases import Databases
from getpass import getpass
from .account import * 

def create_account():
    # Gera a chave de criptografia simétrica
    db = Databases(db_name="databases/users.db", table="users")
    while True:
        # Loop para solicitar usuário e senha enquanto inválidos
        new_user = input("Digite o novo nome de usuário: ").strip()
        new_pass = getpass("Digite sua senha (echo no terminal desabilitado!)").strip()
        verify_pass = getpass("Digite sua senha novamente").strip()
        if new_user == new_pass:
            print("[-] Sua senha não pode ser igual ao nome de usuário!")
            continue
        is_upper = password_has_uppercase(new_pass)    
        if password_verification(new_pass, verify_pass, is_upper):
            # Senha válida, criptografar
            new_pass = encrypt_pass(new_pass)
            db.insert_users(new_user, new_pass)
            break
