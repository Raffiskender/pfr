import hashlib
from src.models.database import Database
import time 
from src.controllers.session_manager import SessionManager
from streamlit_cookies_controller import CookieController

class Session:
    def __init__(self, email, password, name = 'NoName', is_activated = True, is_admin = False) -> None:
        self.logged : bool = False
        self.email : str =  email
        self._password : str = password
        self.name : str = name
        self.is_activated : bool = is_activated
        self.is_admin : bool = is_admin

    def hash(self) -> str:
        return hashlib.sha256(self._password.encode(encoding="utf-32")).hexdigest()

    def getUID(self):
        with Database() as db:
            res = db.execute("SELECT uid FROM users WHERE password=? AND email=?", (self.hash(), self.email))
            return res.fetchone()[0]

    def fetch_user(self) -> bool:
        with Database() as db:
            res = db.execute("SELECT uid, name, email, is_admin, is_activated FROM users WHERE password=? AND email=?", (self.hash(), self.email))
            return res.fetchone()

    def login(self):
        res = self.fetch_user()
        if res:
            with Database() as db:
                db.execute(f"INSERT INTO logs (uid, action, value) VALUES ( ? , \"logged\", ? )", (self.getUID(), int(time.time())))
                db.commit()
            self.logged = True
            self.persist(res)
        else:
            print("User doesn't exist in DB")

    def signin(self):
        if not self.fetch_user():
            with Database() as db:
                db.execute("INSERT INTO users (email, password, name, is_admin, is_activated) VALUES (?, ?, ?, ?, ?)", (self.email, self.hash(), self.name, self.is_admin, self.is_activated))
                db.commit()
            print(f"User {self.email} have been created")
            return True
        else:
            print("User already exist on DB")
            return False

    def persist(self, res):
        cookies_ctrl = CookieController()
        session_mng = SessionManager()
        cookies_ctrl.set('user_session', session_mng.create_token(res))
        