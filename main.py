from accounts_treat.account import account_menu
from accounts_treat.create import create_account
from accounts_treat.login import login
from Databases import Databases
from management.user_menu import user_menu
def main():
    Databases(db_name="databases/users.db", table="users").setup_db()
    Databases(db_name="databases/manager.db", table="manager_passwords").setup_db()

    menu_account_value = account_menu()
    if menu_account_value == "value_error":
        print("[-] Você digitou um valor inválido, certifique-se de digitar 1 ou 2")
    elif menu_account_value == "exception":
        print("[-] Ocorreu um erro desconhecido, tente novamente")
    elif menu_account_value == "create":
        create_account()
    elif menu_account_value == "login":
        is_logged = login()
        if is_logged is not False:
            user_menu(is_logged)
        else:
            user_menu(False)  
        
if __name__ == "__main__":
    main()