import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def correlations(df):
    # Liste des variables numériques
    dropdown_options = df.select_dtypes(include=['number']).columns
    
    # Interface utilisateur
    st.title("Analyse des corrélations")
    selected_vars = st.multiselect("Choisissez les variables à corréler", dropdown_options, default=dropdown_options)

    # Vérifier qu'au moins deux variables sont sélectionnées
    if len(selected_vars) >= 2:
        corr_matrix = df[selected_vars].corr().round(2)
        st.subheader("Matrice de corrélation")
        
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0, linewidths=0.5, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Veuillez sélectionner au moins deux variables.")


def categorial(df):
    st.title('Analyse catérgorielles')

    # Liste des variables catégorielles et numériques
    dropdown_options_numeric = df.select_dtypes(include=['number']).columns
    dropdown_options_categorical = df.select_dtypes(include=['object', 'bool']).columns

    # Interface utilisateur
    st.title("Analyse des Box Plots avec Interaction")

    # Sélectionner la variable numérique
    numeric_var = st.selectbox("Choisissez la variable numérique", dropdown_options_numeric)

    # Sélectionner la variable catégorielle
    categorical_var = st.selectbox("Choisissez la variable catégorielle", dropdown_options_categorical)

    # Affichage des box plots avec sélection des variables
    st.subheader(f"Box plot de {numeric_var} par {categorical_var}")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Option de filtrage pour les données
    age_range = st.slider("Choisissez la plage d'âge", int(df['age'].min()), int(df['age'].max()), (int(df['age'].min()), int(df['age'].max())))
    filtered_data = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]

    # Afficher le box plot filtré
    st.subheader(f"Box plot de {numeric_var} par {categorical_var} (Filtré)")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=categorical_var, y=numeric_var, data=filtered_data, ax=ax)
    st.pyplot(fig)

def radar(df):
    st.title("Analyse avec Graphique en Toile d'Araignée")

    # Liste des variables numériques et catégorielles
    select_options_numeric = ['stress_level', 'caffeine_intake', 'sleep_hours', 'physical_activity', 'alcohol_consuption', 'heart_rate_during_attack','breathing_rate','sweating_level', 'therapy_session', 'diet_quality', 'attack_severity']
    select_options_categorical = ['age', 'occupation', 'gender', 'smoking', 'recent_life_event', 'medication', 'family_history']

    # Sélectionner les variables numériques
    selected_numeric_vars = st.multiselect("Choisissez les variables numériques", select_options_numeric, default=select_options_numeric)

    # Sélectionner les critères de filtrage avec des cases à cocher
    filters = {}
    col1, col2 = st.columns(2)
    with col1:
        for option in select_options_categorical:
            if option == 'age':
                if st.checkbox(f"Filtrer par {option}", key=f"filter_{option}"):
                    age_range = st.slider(
                        "Choisissez la plage d'âge", 
                        int(df[option].min()), 
                        int(df[option].max()), 
                        (int(df[option].min()), int(df[option].max())), 
                        key=f'age_range'
                    )
                    filters[option] = age_range
                    
            elif option == 'gender':
                if st.checkbox(f"Filtrer par {option}", key=f"filter_{option}"):
                    selected_gender = st.multiselect(
                        "Choisissez le sexe", 
                        df[option].unique(),
                        default=df[option].unique(),
                        key=f'select_{option}'
                    )
                    filters[option] = selected_gender
                    
            elif option == 'occupation':
                if st.checkbox(f"Filtrer par {option}", key=f"filter_{option}"):
                    selected_occupation = st.multiselect(
                        "Choisissez le travail", 
                        df[option].unique(),
                        default=df[option].unique(),
                        key=f'select_{option}'
                    )
                    filters[option] = selected_occupation
    with col2:
        for option in select_options_categorical:
            if option != 'age' and option != 'occupation' and option != 'gender' :
                if st.checkbox(f'Filtrer par {option}', key=f"filter_{option}"):
                    radio_choice = st.radio(
                        f"Catégorie {option}", 
                        options=[f'{option}', f'no {option}'],
                        key=f'radio_{option}'
                    )
                    filters[option] = radio_choice
    
    
    # Appliquer les filtres

    filtered_df = df.copy()
    for key, value in filters.items():
        if key == 'age':
            filtered_df = filtered_df[(filtered_df[key] >= value[0]) & (filtered_df['age'] <= value[1])]
        elif key == 'gender' or key == 'occupation':
            filtered_df = filtered_df[filtered_df[key].isin(value)]
        else:
            filtered_df = filtered_df[filtered_df[key] != value.startswith('no')]

    # Interface utilisateur

    # Calcul des moyennes par catégorie filtrée
    category_means = filtered_df[selected_numeric_vars].mean()
    global_means = df[selected_numeric_vars].mean()

    # Préparer les données pour le radar chart
    labels = category_means.index
    values = category_means.values
    global_values = global_means.values
    
    
    # Créer le graphique en toile d'araignée
    angles = [n / float(len(labels)) * 2 * np.pi for n in range(len(labels))]
    scalled_values = np.array([])
    scalled_global_values = np.array([])

    for value, global_value, label in zip(values, global_values, labels):
        scalled_values = np.append(scalled_values, (value / (df[label].max())))
        scalled_global_values = np.append(scalled_global_values, (global_value / (df[label].max())))
    
    labels = np.append(labels, labels[0])
    angles = np.append(angles, angles[0])
    scalled_values = np.append(scalled_values, scalled_values[0])
    scalled_global_values = np.append(scalled_global_values, scalled_global_values[0])

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # Tracer les valeurs filtrées
    ax.plot(angles, scalled_values, color='blue', linewidth=1, linestyle='solid', label='Moyennes')
    # Tracer les valeurs globales
    ax.plot(angles, scalled_global_values, color='grey', linewidth=1, linestyle='solid', label='Moyennes')

    # Remplir le graphique
    # ax.fill(angles, scalled_values, alpha=0.3)
    # ax.fill(angles, scalled_global_values, alpha=0.3)

    # Ajouter les labels et les titres
    #ax.set_ylim(0, 100)
    ax.set_yticklabels([])
    ax.set_xticks(angles)
    ax.set_xticklabels(labels)

    ax.legend(loc='upper right', labels=['Filtré', 'Global'], bbox_to_anchor=(1.2, 1.1))
    # Affichage
    st.subheader("Graphique en toile d'araignée selon les critères séléctionnés")
    st.pyplot(fig)


def load():
    st.title('Visualisation')
    st.write(
    '''
    Ci dessous quelques visualisations intéressante
    ''')

    df_org = pd.read_csv('./src/assets/data/anxiety_attack_dataset.csv')
    df = pd.read_csv('./src/assets/data/clean_data.csv')
    df['occupation'] = df_org['Occupation']
    df['gender'] = df_org['Gender']
    
    with st.expander('Visualiser les correlations'):
        correlations(df)
    with st.expander('visualiser les catégories'):
        categorial(df)
    with st.expander('visualiser les moyennes filtrées'):
        radar(df)

load()