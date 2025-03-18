import hashlib
from src.models.database import Database
import time 
import json

class Session:
    def __init__(self, email, password) -> None:
        self.logged : bool = False
        self.email : str =  email
        self._password : str = password

    def hash(self) -> str:
        return hashlib.sha256(self._password.encode(encoding="utf-32")).hexdigest()

    def exist(self) -> bool:
        with Database() as db:
            res = db.execute("SELECT uid FROM users WHERE password=? AND email=?", (self.hash(), self.email))
            return res.fetchone() is not None

    def getUID(self):
        with Database() as db:
            res = db.execute("SELECT uid FROM users WHERE password=? AND email=?", (self.hash(), self.email))
            return res.fetchone()[0]

    def login(self):
        if self.exist():
            with Database() as db:
                db.execute(f"INSERT INTO logs (uid, action, value) VALUES ( ? , \"logged\", ? )", (self.getUID(), int(time.time())))
                db.commit()
            self.logged = True
        else:
            print("User doesn't exist in DB")

    def signin(self):
        if not self.exist():
            with Database() as db:
                db.execute(f"INSERT INTO users (email,password) VALUES ('{self.email}', '{self.hash()}')")
                db.commit()
            print("User have been created")
            return True
        else:
            print("User already exist on DB")
            return False

    def persist(self):
        data = {
                "email" : self.email
        }
        with open("session.json", 'w') as outfile:
            json.dump(data, outfile)
