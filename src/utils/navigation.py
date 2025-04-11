import streamlit as st

class Navigation:
    def __init__(self):

        self.home_page       = st.Page('src/views/home.py', title="Home", icon=":material/home:", default=True)
        self.login_page      = st.Page('src/views/user_mngt/login.py', title="Log in", icon=":material/login:")
        self.logout_page     = st.Page('src/views/user_mngt/logout.py', title="Log out", icon=":material/logout:")
        self.account_page    = st.Page("src/views/user_mngt/account.py", title="Account", icon=":material/person:")
        self.signin_page     = st.Page("src/views/user_mngt/signin.py", title="Sign in", icon=":material/gesture:")
        self.cleaning_page   = st.Page('src/views/private/cleaning.py', title="Nettoyage", icon=":material/mop:")
        self.conclusion_page = st.Page('src/views/private/conclusion.py', title="Conclusion", icon=":material/menu_book:")
        self.eda_page        = st.Page('src/views/private/eda.py', title="Analyse", icon=":material/analytics:")
        self.viz_page        = st.Page('src/views/private/viz.py', title="Visualisations", icon=":material/scatter_plot:")
        self.options_page    = st.Page("src/views/private/options.py", title="Options", icon=":material/settings:")
        self.admin_page      = st.Page("src/views/admin/admin.py", title="Admin", icon=":material/key:")

        # self.user_navigation()
        
    def user_navigation(self):

        user_connected_pages = [self.home_page, self.cleaning_page, self.eda_page,self.viz_page, self.conclusion_page]
        user_mngt_pages      = [self.logout_page, self.options_page, self.account_page]
        user_admin_pages     = [self.admin_page]

        page_dict = {}

        if 'user' not in st.session_state or st.session_state.user is None:
            return st.navigation({"Navigation": [self.home_page], "Account":[self.login_page, self.signin_page]})
        else:
            if "viewer" in st.session_state['user']['roles'] and "admin" in st.session_state['user']['roles']:
                page_dict["Navigation"] = user_connected_pages
                page_dict["Account"] = user_mngt_pages
                page_dict["Admin"] = user_admin_pages
                return st.navigation(page_dict)
            elif "viewer" in st.session_state['user']['roles']:
                page_dict["Navigation"] = user_connected_pages
                page_dict["Account"] = user_mngt_pages
                return st.navigation(page_dict)