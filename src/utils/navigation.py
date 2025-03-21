import streamlit as st
import base64

from streamlit.components.v1 import html

from PATHS import NAVBAR_PATHS, SETTINGS

class Navigation():
    def __init__(self):
        pass

    def display_navbar(self):

        with open("src/assets/images/settings.png", "rb") as image_file:
            image_as_base64 = base64.b64encode(image_file.read())
        navbar_items = ''
        settings_items = ''

        nav_bar_items_burger = ''
        settings_items_burger = ''

        if "SESSION_LOGGED" not in st.session_state or not st.session_state.SESSION_LOGGED :
            for key, value in NAVBAR_PATHS.items():
                if (key != "ACCUEIL"):
                    #nav wide
                    navbar_items += (
                        f'<a style="display: none" target="_self" href="/?page={value}" class="navitem">{key}</a>')
                    #nav burger
                    nav_bar_items_burger += (
                        f'<li style="display: none" class="nav__list_item"><a target="_self" class="navitem" href="/?page={value}">{navbar_items}</a></li>')
                else:
                    #nav wide
                    navbar_items += (
                        f'<a style="display: flex" target="_self" href="/?page={value}" class="navitem">{key}</a>')
                    #nav burger
                    nav_bar_items_burger += (
                        f'<li style="display: flex" class="nav__list_item"><a target="_self" class="navitem" href="/?page={value}">{navbar_items}</a></li>')

            for key, value in SETTINGS.items():
                if (key != "CONNEXION"):
                    #nav wide
                    settings_items += (
                        f'<a style="display: none" target="_self" href="/?page={value}" class="settingsNav">{key}</a>')
                    #nav burger
                    settings_items_burger += (
                        f'<a style="display: none" target="_self" href="/?page={value}" class="settingsNav">{key}</a>')
                else:
                    #nav wide
                    settings_items += (
                        f'<a style="display: flex" target="_self" href="/?page={value}" class="settingsNav">{key}</a>')
                    #nav burger
                    settings_items_burger += (
                        f'<a style="display: flex" target="_self" href="/?page={value}" class="settingsNav">{key}</a>')
        else:
            for key, value in NAVBAR_PATHS.items():
                #nav wide
                navbar_items += (
                    f'<a style="display: flex" target="_self" class="navitem" href="?page={value}">{key}</a>')
                #nav burger
                nav_bar_items_burger += (
                    f'<li style="display: flex" class="nav__list_item"><a target="_self" class="nav__link" href="/?page={value}">{navbar_items}</a></li>')

            for key, value in SETTINGS.items():
                if (key == "CONNEXION"):
                    #nav wide
                    settings_items += (
                        f'<a style="display: none" target="_self" href="/?page={value}" class="settingsNav">{key}</a>')
                    #nav_burger
                    settings_items_burger += (
                        f'<a style="display: none" target="_self" href="/?page={value}" class="settingsNav">{key}</a>')
                else:
                    #nav_wide
                    settings_items += (
                        f'<a style="display: flex" target="_self" href="/?page={value}" class="settingsNav">{key}</a>')
                    #nav burger
                    settings_items_burger += (
                        f'<a style="display: flex" target="_self" href="/?page={value}" class="settingsNav">{key}</a>')


        navigation = rf'''
        <div>
            <div class="nav_burger_btn">
                <span class="burger_bar"></span>
                <span class="burger_bar"></span>
                <span class="burger_bar"></span>
            </div>
        </div>
        <nav class="navbar_burger">
            <ul class="burger_nav__list">
                {navbar_items}
                <span class="burger_separation" ></span>
                {settings_items}
            </ul>
        </nav>

        <nav class="container navbar_wide" id="navbar">
            <ul class="navlist_wide">
                {navbar_items}
                <div class="dropdown" id="settingsDropDown">
                    <img class="dropbtn" src="data:image/png;base64, {image_as_base64.decode("utf-8")}"/>
                    <div style= "visibility: hidden" id="myDropdown" class="dropdown-content">
                        {settings_items}
                    </div>
                </div>
            </ul>
        </nav>
        '''

        st.markdown(navigation, unsafe_allow_html=True)

        js = '''
        <script>
            // Dropdown hide / show

            var dropdown = window.parent.document.querySelector("img.dropbtn");
            var dropWindow = window.parent.document.getElementById("myDropdown")
            dropdown.onclick = () => {
                if (dropWindow.style.visibility == "hidden"){
                    dropWindow.style.visibility = "visible";
                    window.parent.document.addEventListener('click', (event) => {
                        console.log(event.target)
                        if (event.target != dropdown ){
                            console.log('Perte de focus sur dropdown');
                            dropWindow.style.visibility = "hidden";
                            }
                    }, once=true);
                }else{
                    dropWindow.style.visibility = "hidden";
                }
            };

            // Burger menu hide / show
            var burger_btn = window.parent.document.querySelector(".nav_burger_btn");
            var burger_nav = window.parent.document.querySelector(".navbar_burger");

            burger_btn.onclick = () => {
                burger_btn.classList.toggle("active");
                burger_nav.classList.toggle("active");
            }
        </script>
        '''
        html(js)
