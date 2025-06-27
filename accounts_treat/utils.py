import re
import hashlib
import os
from cryptography.fernet import Fernet


def account_menu():
    # Função para exibir o menu de opções
    print("Bem-vindo ao seu gerenciador de senhas!\n")
    print("[1] Criar conta!\n")
    print("[2] Fazer login!\n")

    try:
        option = int(input("> "))
    except ValueError:
        return "value_error"
    if option == 1:
        return "create"
    elif option == 2: 
        return "login"
    else: 
        return "exception"

def password_has_uppercase(password):
    return any(char.isupper() for char in password)

def encrypt_hash(password):
    # Gera o hash da senha
    signature = hashlib.sha256(password.encode()).hexdigest()
    return signature    

def create_key():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(BASE_DIR, "key.key")
    if os.path.exists(key_path) and os.path.getsize(key_path) > 0:
        with open(key_path, "rb") as existing_content:
            return existing_content.read()
    else:
        key = Fernet.generate_key() 
        with open(key_path, "wb") as file:
            file.write(key)
            return key
def load_key():
    return create_key()

def encrypt_pass(password):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()


def decrypt_pass(password):
    key = load_key()    
    fernet = Fernet(key)
    return fernet.decrypt(password.encode()).decode() 

def password_verification(password, password_again, upper):
    # função de verificação
    special_chars = set(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
    if len(password) < 8:
        print("[-] A senha deve ter mais de 8 caracteres")
        return False
    elif re.search("[0-9]", password) is None:
        print("[-] A senha precisa ter ao menos um número")
        return False
    elif not special_chars.intersection(password):
        print("[-] A senha precisa de ao menos um caracter especial")
        return False
    elif not upper:
        print("[-] A senha precisa ter ao menos um caracter maiúsculo")
        return False
    elif password.isnumeric():
        print("[-] A senha não pode ser composta apenas por números")        
        return False
    elif password != password_again:
        print("[-] As senhas não coincidem")
        return False
    else:
        return True    

def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
