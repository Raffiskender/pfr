import streamlit as st
from src.models.database import Database
import hashlib
import ast

class UserModel(Database):
    def __init__(self, login, password):
        super().__init__()

        self.username : str = login
        self.password : str = self.hash(password)
        self.email : str = ''
        self.roles : list = []
    
    def hash(self, pw) -> str:
        return hashlib.sha256(pw.encode(encoding="utf-32")).hexdigest()
    
    def find_by_email_or_username(self):
        try:
            response = self.execute(
                f"""
                SELECT id, username, email, roles
                FROM {self.users_table}
                WHERE ({self.users_table}.username = ? OR {self.users_table}.email = ?) AND {self.users_table}.password = ?""",
                (self.username, self.username, self.password)).fetchone()
            
            if response:
                self.update_user_from_db_values(response)
                return self
            return None
            
        except Exception as response:
            return f"Erreur : {response}"

    def update_user_from_db_values(self, data):
        self.set_id(data[0])
        self.set_username(data[1])
        self.set_email(data[2])
        self.set_roles(ast.literal_eval(data[3]))

    # Les getters
    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_roles(self):
        return self.roles

    #Les setters
    def set_id(self, value):
        self.id = value
        
    def set_username(self, value):
        self.username = value

    def set_email(self, value):
        self.email = value

    def set_roles(self, value):
        self.roles = value
