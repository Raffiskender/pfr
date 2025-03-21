import streamlit as st
from src.controllers.auth import logout
from src.router import redirect
import streamlit.components.v1 as components

def load_view():
    logout()
    clear_cookies_js()

    redirect("home", reload=True)
             
def clear_cookies_js() :
    js_code = """
        <script>
        document.cookie.split(";").forEach((c) => {
            document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/");
        });
        window.location.reload();
        </script>
    """
        
    components.html(js_code)
