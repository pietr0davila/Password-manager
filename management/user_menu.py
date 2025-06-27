from .passwords.add_password import add_password
from .passwords.list_password import list_password
from .passwords.remove_password import remove_password
from accounts_treat.utils import clear_terminal

def user_menu(user_id, username):
    if isinstance(user_id, int):
        while True:
            print(f"Bem-vindo, {username}\n")
            print("---- CENTRAL DE GERENCIAMENTO ----\n")
            print("[1] Adicionar senhas")
            print("[2] Remover senhas")
            print("[3] Listar senhas")
            print("[4] Sair")
            try:
                action = int(input("> "))
                if action == 1:
                    clear_terminal()
                    add_password(user_id)
                    continue
                elif action == 2:
                    clear_terminal()
                    remove_password(user_id)
                    continue                
                elif action == 3:
                    clear_terminal()
                    list_password(user_id)    
                    continue
                else:
                    print("[-] Saindo...")
                    exit(0)
            except ValueError:
                print("[-] Você digitou uma opção inválida!")
                continue
            
    else:
        print("[-] Sentimos muito pelo erro, parece que você não está logado")