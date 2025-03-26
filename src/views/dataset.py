import streamlit as st
import pandas as pd
import base64

def load_view():
    st.title('Aquisition, préparation et présentation des données')

    df = pd.read_csv('./data/anxiety_attack_dataset.csv')
    df_clean = pd.read_csv('./data/clean_data.csv')
    
    st.markdown(
        """
        ## Données sur les crises d'anxiété"
        Ci-dessous les données brutes chargées depuis un dataset Kaggle.
    """)
    with st.expander("Afficher les données brutes"):
        st.dataframe(df)
    
    st.markdown(
        """
        ## Préparation
        
        Ci-dessous les données nettoyées. Notez qu'elles étaient propres à l'origine.J'ai juste ajouté quelques get_dummies pour faciliter l'exploiattion des données.
        J'ai également renommé quelques colonnes pour qu'elles soient plus consises.
    """)
    with st.expander("Afficher les données nettoyées"):
        st.dataframe(df_clean)

    with open("src/assets/images/db_diagram.png", "rb") as image_file:
            image_as_base64 = base64.b64encode(image_file.read())

    st.markdown(
        f"""
        
        ## Insertion en base de donnée

        Les données présentée ci-dessus ont été triés par catégories et insérées dans une base de donnée dont le diagramme et les diverses relations sont exposées sur le schémas ci-dessous.
        <img class="db_diagram_img" src="data:image/png;base64, {image_as_base64.decode("utf-8")}" alt="Diagramme de la base de données"/>
        
        exemple d'insertion du css vers la base de donnée :
    """, unsafe_allow_html=True)

    st.code('''
        # Création de la table patients - code SQL:
        CREATE TABLE IF NOT EXISTS patient(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            gender_is_male INTEGER, # Les booléens sont des integers dans sqlite.
            gender_is_female INTEGER,
            gender_is_other INTEGER)

        # Lecture du CSV
        df = pd.read_csv("./data/clean_data.csv")

        # Insertion des données dans la table
        # L'objet database est le modèle de l'application. Je me sers ici de sa fonction
        # execute qui reçois 2 arguments : la requette et ses paramètres.
            
        with Database() as db:
            for _, row in df.iterrows():
                cur = db.execute(\'\'\'
                INSERT INTO patient (age, gender_is_male, gender_is_female, gender_is_other)
                VALUES (?, ?, ?, ?)\'\'\',
                (row['age'], row['gender_Male'], row['gender_Female'], row['gender_Other']))
            db.commit()
    ''')
    st.markdown(
        """
        Ce code a été mis dans un fichier d\'extension .py. Il doit être executé manuellement (`python3 data_to_db.py`).

        ## Description des données

        Les données présentent les données de 12000 sur des patients ayant eu une crise d'anxiété. Les colonnes sont les suivantes:
        - Age
        - Sexe
        - Métier
        - Heures de sommeil
        - Activité physique
        - Consommation de caféine
        - Consommation d'alcool
        - Tabagisme
        - Antécédents familiaux
        - Niveau de stress
        - Fréquence cardiaque pendant une crise
        - Fréquence respiratoire
        - Niveau de transpiration
        - Étourdissements
        - Médication
        - Séance de thérapie
        - Événement de vie récent
        - Qualité de l’alimentation
        - Gravité de la crise
                    
    """)