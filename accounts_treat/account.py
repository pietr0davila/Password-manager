import re
import hashlib

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

def encrypt_pass(password):
    # Gera o hash da senha
    signature = hashlib.sha256(password.encode()).hexdigest()
    return signature    

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
