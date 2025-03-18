import sqlite3

class Database :
    def __init__(self) -> None:
        self.__db_path = "project.db"
        self.__db = None

    def __enter__(self):
        self.__db = sqlite3.connect(self.__db_path)
        return self.__db

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__db:
            self.__db.close()

    def setup(self):
        self.execute("""CREATE TABLE IF NOT EXISTS users(
                     uid INTEGER PRIMARY KEY UNIQUE,
                     email VARCHAR UNIQUE,
                     password VARCHAR)""", ())
        self.execute("""CREATE TABLE IF NOT EXISTS logs(
                     id INTEGER PRIMARY KEY UNIQUE,
                     uid INTERGER,
                     action VARCHAR,
                     value VARCHAR)""", ())
        try:
            self.execute("INSERT INTO users (email,password) VALUES ('admin', 'admin')", ())
        except:
            print("Admin already exists.")
        self.commit()


    # def drop(self):
    #     self.execute("DROP TABLE ? ", ("users"))
    #     self.execute("DROP TABLE ? ", ("logs"))
    #     self.commit()

    def execute(self, query:str, values:tuple=()):
        return self.__db.cursor().execute(query, values)

    def commit(self):
        return self.__db.commit()
