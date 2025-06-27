from accounts_treat.utils import account_menu
from accounts_treat.create import create_account
from accounts_treat.login import login
from Databases import Databases
from management.user_menu import user_menu
from cryptography.fernet import Fernet

def main():
    key = Fernet.generate_key()
    with open("key.secret", "wb") as file:
        file.write(key)

    Databases(db_name="databases/users.db", table="users").setup_user_db()
    Databases(db_name="databases/manager.db", table="manage_passwords").setup_password_db()

    menu_account_value = account_menu()
    if menu_account_value == "value_error":
        print("[-] Você digitou um valor inválido, certifique-se de digitar 1 ou 2")
    elif menu_account_value == "exception":
        print("[-] Ocorreu um erro desconhecido, tente novamente")
    elif menu_account_value == "create":
        create_account()
    elif menu_account_value == "login":
        user_id, username = login()
        if isinstance(user_id, int):
            user_menu(user_id, username)
        else:
            user_menu(False, False)  
        
if __name__ == "__main__":
    main()