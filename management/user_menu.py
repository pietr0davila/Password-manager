def user_menu(username):
    if username:
        print(f"Bem-vindo, {username}")
        print("---- CENTRAL DE GERENCIAMENTO ----")
        print("[1] Adicionar senha")
        print("[2] Remover senha do catálogo")
        print("[3] Sair")
    else:
        print("[-] Sentimos muito pelo erro, parece que você não está logado")