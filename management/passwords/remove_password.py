from Databases import Databases
from . import list_password
db = Databases(db_name="databases/manager.db", table="manage_passwords")

def init_database():
    db.setup_password_db()

def remove_password(user_id):
    init_database()
    select = input("Digite o serviço que deseja apagar (pressione 1 para ver os disponíveis)")
    if select == "1":
        list_password.list_password(user_id)
    else:
        print(f"serviço {select} removido com sucesso!")
        db.remove_passwords(user_id, select)
