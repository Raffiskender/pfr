import sqlite3
import hashlib

class Database :
    def __init__(self) -> None:
        self.__db_path = "project.db"
        self.__db = None
        self.users_table = "users"

    def __enter__(self):
        self.__db = sqlite3.connect(self.__db_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__db:
            self.__db.close()

    def setup_users_table(self):
        self.execute(
        f'''
            CREATE TABLE IF NOT EXISTS {self.users_table}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR UNIQUE,
                email INTEGER UNIQUE,
                first_name INTEGER,
                last_name INTEGER,
                password INTEGER,
                roles VARCHAR
                )
        ''', ())
        self.commit()
        print('tables created')
        print(self.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
        
    def create_user_raffi(self):
        # The hash method from Hasher class is the one used by streamlit-authenticator.
        try:
            self.execute(f"""INSERT INTO {self.users_table} (username, email, password, roles)
                VALUES (?, ?, ?, ?)
                """, ('Mika', 'mika@sken.com', hashlib.sha256("123".encode(encoding="utf-32")).hexdigest(), "['viewer']"))
            self.commit()
            print('utilisateur "Mika" créé avec succès')
        except Exception as e:
            print(f"Erreur : {e}")

    def drop_users_table(self):
        self.execute(f"DROP TABLE IF EXISTS {self.users_table}")
        self.commit()

    def drop_all_tables(self):
        self.execute("DROP TABLE IF EXISTS patient, health, life_style, attack, users, logs")
        self.commit()

    def execute(self, query:str, values:tuple=()):
        return self.__db.cursor().execute(query, values)

    def commit(self):
        return self.__db.commit()

    def get_connection(self):
        return self.__db