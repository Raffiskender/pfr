import streamlit as st

def load():
    st.title('Conclusion')
    st.markdown(
    '''
        ## Qu'avons-nous fait ?
        ### 🛠️ Présentation et nettoyage des données
        Nous avons commencé par une **exploration** du jeu de données, en identifiant ses principales caractéristiques, puis e **data cleaning** a permis d'assurer une **meilleure qualité des données** en appliquant plusieurs étapes :  
        - Analyse des valeurs manquantes et des incohérences  
        - Identification des **variables numériques et catégorielles**
        - Transformations des catégories en get_dummies
        - **Gestion des valeurs manquantes ou des incohérences** : Par chance il n'y en n'avait pas

        ### 📊 Analyse Exploratoire des Données (EDA)  
        L’**EDA (Exploratory Data Analysis)** a mis en lumière les **tendances et corrélations** grâce à plusieurs techniques :  
        - Création d'un dataframe depuis une base de donnée  
        - **Comparaison des moyennes** par groupe avec des graphiques
        - **vérification des répartitions** avec des graphiques adaptés

        ### 📈 Visualisation Interactive  
        Une partie importante de ce projet a été dédiée à la **visualisation interactive**, permettant à l'utilisateur de :
        - **Explorer les données** en temps réel avec des filtres dynamiques (cases à cocher, sliders, etc.)  
        - **Analyser les moyennes des variables** filtrées, avec une **visualisation radar** permettant une comparaison facile entre les différentes catégories.  


        🏆 **Nos données sont désormais propres, analysables et prêtes pour des insights !** 🔥  

    ''')