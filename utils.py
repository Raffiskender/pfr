import streamlit as st
import base64
from streamlit.components.v1 import html

from PATHS import NAVBAR_PATHS, SETTINGS


def inject_custom_css():
    with open('src/assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def navbar_component():
    with open("src/assets/images/settings.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())
    navbar_items = ''
    settings_items = ''

    if st.session_state.SESSION.get('email') != "":
        for key, value in NAVBAR_PATHS.items():
            navbar_items += (f'<a style="visibility: visible" target="_self" class="navitem" href="/?nav=/{value}">{key}</a>')

        for key, value in SETTINGS.items():
            if (key == "CONNEXION"):
                settings_items += (
                f'<a style="display: none" target="_self" href="/?nav=/{value}" class="settingsNav">{key}</a>')
            else:
                settings_items += (
                f'<a style="display: flex" target="_self" href="/?nav=/{value}" class="settingsNav">{key}</a>')
                
    else:
        for key, value in NAVBAR_PATHS.items():
            if (key != "ACCUEIL"):
                navbar_items += (
                f'<a style="display: none" target="_self" href="/?nav=/{value}" class="navitem">{key}</a>')
            else:
                navbar_items += (
                f'<a style="display: flex" target="_self" href="/?nav=/{value}" class="navitem">{key}</a>')

        for key, value in SETTINGS.items():
            if (key != "CONNEXION"):
                settings_items += (
                f'<a style="display: none" target="_self" href="/?nav=/{value}" class="settingsNav">{key}</a>')
            else:
                settings_items += (
                f'<a style="display: flex" target="_self" href="/?nav=/{value}" class="settingsNav">{key}</a>')

    component = rf'''
            <nav class="container navbar" id="navbar">
                <ul class="navlist">
                    {navbar_items}
                </ul>
                <div class="dropdown" id="settingsDropDown">
                    <img class="dropbtn" src="data:image/png;base64, {image_as_base64.decode("utf-8")}"/>
                    <div style= "visibility: hidden" id="myDropdown" class="dropdown-content">
                        {settings_items}
                    </div>
                </div>
            </nav>
            '''
    st.markdown(component, unsafe_allow_html=True)

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
    </script>
    '''
    html(js)
