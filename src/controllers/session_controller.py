from streamlit_cookies_controller import CookieController
from src.models.session_model import SessionModel
import time
import streamlit as st

class SessionController:
    def __init__(self):
        self.cookie_name = 'user_session'

    def persist(self, user):
        try:
            cookies_ctrl = CookieController()
            cookies_ctrl.set(self.cookie_name, SessionModel().create_token(user))
            # Patienter 50ms le temps de la création du cookie avant le changement de page
            time.sleep(0.5) 
            return True,
        except Exception as e:
            return False, e
        
    def retrieve_user_cookie(self):
        print()
        

    
    def check_user(self):
        try:
            token = st.context.cookies[self.cookie_name]
            if token:
                try :
                    user = SessionModel().decode_token(token)
                    self.persist_user(user)
                except Exception as e:
                    print(e)
                    return token
            return False
        
        except KeyError as e:
            print(f"Pas de cookie nommé {e}")

        return False

    def persist_user(self, user):
        st.session_state['user'] = {
                'id' : user['id'],
                'username' : user['username'],
                'email' : user['email'],
                'roles' : user['roles']
            }
        st.session_state['is_logged'] = True

            