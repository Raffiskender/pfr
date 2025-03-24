import sqlite3
import hashlib

class Database :
    def __init__(self) -> None:
        self.__db_path = "project.db"
        self.__db = None

    def __enter__(self):
        self.__db = sqlite3.connect(self.__db_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__db:
            self.__db.close()

    def setup(self):
        self.execute("""CREATE TABLE IF NOT EXISTS users(
                     uid INTEGER PRIMARY KEY UNIQUE,
                     email VARCHAR UNIQUE,
                     name VARCHAR UNIQUE,
                     is_admin BOOLEAN,
                     is_activated BOOLEAN,
                     password VARCHAR)""", ())
        self.execute("""CREATE TABLE IF NOT EXISTS logs(
                     id INTEGER PRIMARY KEY UNIQUE,
                     uid INTERGER,
                     action VARCHAR,
                     value VARCHAR)""", ())
        try:
            self.execute("INSERT INTO users (email, password, name, is_admin, is_activated) VALUES (?, ?, ?, ?, ?)", ('admin', hashlib.sha256("Admin1234".encode(encoding="utf-32")).hexdigest(), "Admin", 0, 0))
            print("Admin user Created")
        except Exception as e:
            print("Admin already exists.")
            print(e)
        self.commit()


    def drop(self):
        self.execute("DROP TABLE users")
        self.execute("DROP TABLE logs")
        self.commit()

    def execute(self, query:str, values:tuple=()):
        return self.__db.cursor().execute(query, values)

    def commit(self):
        return self.__db.commit()

    