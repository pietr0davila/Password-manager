import sqlite3
import hashlib

class Databases:
    def __init__(self, db_name, table):
        self.db_name=db_name
        self.table=table
    
    def setup_db(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.table} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    hash TEXT NOT NULL 
                );
                ''')
        except sqlite3.OperationalError as e:
            print("[-] Não foi possível iniciar o banco de dados, sentimos muito!", e)

    
    def get_connection(self):
        return sqlite3.connect(self.db_name)
    
    def insert_users(self, username, password):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                query = f"INSERT INTO {self.table} (username, hash) VALUES (?, ?)"
                cursor.execute(query, (username, password))
                conn.commit()
                print("[+]Sua conta foi criada com sucesso, ", username, "!")
            except sqlite3.IntegrityError:
                print("[-] Que pena, parece que esse nome de usuário já foi usado, tente novamente!")
    def get_users(self, username, password):
        compare_hash = hashlib.sha256(password.encode()).hexdigest()
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {self.table} WHERE username = ?"
            cursor.execute(query, (username,))
            found = cursor.fetchone()
            if found:
                hash_found = found[2]
                if hash_found == compare_hash:
                    return True         
                else:
                    return "invalid_pass"
            else:
                return "non_existent_user"


