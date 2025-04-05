import streamlit as st
import pandas as pd
import base64
import nbformat
from nbconvert import PythonExporter

def load():
    st.title('Aquisition, préparation et présentation des données')

    df = pd.read_csv('./src/assets/data/anxiety_attack_dataset.csv')
    df_clean = pd.read_csv('./src/assets/data/clean_data.csv')
    
    st.markdown(
    """
    ## Données sur les crises d'anxiété"
    Ci-dessous les données brutes chargées depuis un dataset Kaggle.
    """)
    with st.expander("Afficher les données brutes"):
        st.dataframe(df)
    
    st.subheader("Présentation des données")
    
    # Charger un notebook
    with open("./src/assets/html_views/notebook.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    st.components.v1.html(html_code, height=600, scrolling=True)

    st.markdown(
        """
        ## Préparation
        
        Les données nettoyées. Notez qu'elles étaient propres à l'origine.J'ai juste ajouté quelques get_dummies pour en faciliter l'exploitation. J'ai également renommé quelques colonnes pour que leur nom soit plus consis.
    """)

    with st.expander('ex. de nettoyage de code'):
        st.code(
        '''
        # Renommage des colonnes
        new_col_names = {
            'Age'                               : 'age',
            'Gender'                            : 'gender',
            'Occupation'                        : 'occupation',
            'Sleep Hours'                       : 'sleep_hours',
            'Physical Activity (hrs/week)'      : 'physical_activity',
            'Caffeine Intake (mg/day)'          : 'caffeine_intake',
            (...)
        }
        df = df.rename(columns=new_col_names)
        
        # Get_dummies
        df = pd.get_dummies(df, columns=['gender'])

        # Transformation des colonnes yes/no en booléens
        yes_no_to_bool = {'Yes': True, 'No': False}
        df['smoking'] = df['smoking'].map(yes_no_to_bool)
        df['family_history'] = df['family_history'].map(yes_no_to_bool)
        df['medication'] = df['medication'].map(yes_no_to_bool)
        df['dizziness'] = df['dizziness'].map(yes_no_to_bool)
        df['recent_life_event'] = df['recent_life_event'].map(yes_no_to_bool)
        ''')

    with st.expander("Afficher les données nettoyées"):
        st.dataframe(df_clean)

    st.markdown(
    """
        
    ## Insertion en base de donnée

    Les données présentée ci-dessus ont été triés par catégories et insérées dans une base de donnée dont le diagramme et les diverses relations sont exposées sur le schémas ci-dessous.
    """)

    st.image("src/assets/images/db_diagram.png", caption="diagramme de la base de données")
        
    st.markdown(
    """
        Puis les tables ont été créées, et les lignes insérées.

        Exemple du code d'insertion du csv vers la base de donnée :
    """)

    st.code('''
        # Création de la table patients - requète SQL seule :
        CREATE TABLE IF NOT EXISTS patient(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            gender_is_male INTEGER, # Les booléens sont des integers dans sqlite.
            gender_is_female INTEGER,
            gender_is_other INTEGER)

        # Lecture du CSV
        df = pd.read_csv("./src/assets/data/clean_data.csv")

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
        Ce code a été mis dans un fichier d\'extension .py qui doit être executé manuellement (`python3 data_to_db.py`).
    """)
        