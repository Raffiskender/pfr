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
    
    def check_user(self):
        try:
            token = st.context.cookies[self.cookie_name]
            if token:
                try :
                    user = SessionModel().decode_token(token)
                    return(user)
                except Exception as e:
                    print(e)
                    return token
            return False
        
        except KeyError as e:
            print(f"Pas de cookie nommé {e}")

        return False
    
    def logout(self):
        st.session_state['user'] = None
        print("from session_controler : sst_User : ", st.session_state['user'])
        self.remove_user_cookie()
        
    def remove_user_cookie(self):
        cookies_ctrl = CookieController()
        try:
            cookies_ctrl.remove(self.cookie_name)
        except Exception as e:
            print(f'Erreur : {e}')
