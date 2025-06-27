import sqlite3
import hashlib

class Databases:
    def __init__(self, db_name, table):
        self.db_name=db_name
        self.table=table
    def setup_password_db(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                service TEXT,
                username TEXT,
                password TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
                );             
                ''')
        except sqlite3.OperationalError as e:
            print("[-] Não foi possível iniciar o banco de dados, sentimos muito", e)
    def setup_user_db(self):
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
                print("[+]Sua conta foi criada com sucesso,", username, "!")
            except sqlite3.IntegrityError:
                print("[-] Que pena, parece que esse nome de usuário já foi usado, tente novamente!")
    def get_users(self, username, password):
        compare_hash = hashlib.sha256(password.encode()).hexdigest()
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT hash, id FROM {self.table} WHERE username = ?"
            cursor.execute(query, (username,))
            found = cursor.fetchone()
            if found:
                hash_found = found[0]
                user_id = found[1]
                if hash_found == compare_hash:
                    return username, user_id
                else:
                    return False, "invalid_pass"
            else:
                return False, "non_existent_user"

    def add_passwords_to_database(self, user_id, service, username, password):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                query = f"INSERT INTO {self.table} (user_id, service, username, password) VALUES (?, ?, ?, ?)"
                cursor.execute(query, (user_id, service, username, password,))
                print(user_id)
                print("[+] Senha adicionada com sucesso")
                conn.commit()
            except Exception as e:
                print("[-] Não foi possível adicionar a senha, sentimos muito", e) 
    def list_passwords(self, user_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT service, username, password FROM {self.table} WHERE user_id = ?"
            cursor.execute(query, (user_id,))
            print(user_id)
            return cursor.fetchall()
    def remove_passwords(self, user_id, service):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                query = f"SELECT * FROM {self.table} WHERE user_id = ? AND service = ?"
                cursor.execute(query, (user_id, service))
                service_exists = cursor.fetchone()
                if service_exists:
                    delete = f"DELETE FROM {self.table} WHERE user_id = ? AND service = ?"
                    cursor.execute(delete, (user_id, service))
                    conn.commit()
                else:
                    print("[-] O serviço que você tentou deletar não existe")
            except Exception as e:
                print("[-] Ocorreu um erro ao remover a senha: ", e)
