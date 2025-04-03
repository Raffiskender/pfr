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
    for option in select_options_categorical:
        filters[option] = st.checkbox(f"Filtrer par {option}")

    # Appliquer les filtres
    filtered_df = df
    for key, is_filter_selected in filters.items():
        if is_filter_selected:
            if key == 'gender':
                selected_gender = st.selectbox("Choisissez le sexe", df[key].unique())
                filtered_df = filtered_df[filtered_df[key] == selected_gender]
            else:
                selected_category = st.selectbox(f"Choisissez la catégorie de {key}", df[key].unique())
                filtered_df = filtered_df[filtered_df[key] == selected_category]






    # Interface utilisateur
    st.title("Analyse avec Graphique en Toile d'Araignée")

    # Sélectionner les variables numériques
    selected_numeric_vars = st.multiselect("Choisissez les variables numériques", select_options_numeric, default=select_options_numeric)

    # Sélectionner le critère de filtrage
    filter_criterion = st.selectbox("Filtrer par", select_options_categorical)

    # Filtrage des données
    if filter_criterion == 'age':
        age_range = st.slider("Choisissez la plage d'âge", int(df['age'].min()), int(df['age'].max()), (int(df['age'].min()), int(df['age'].max())), key='radar_age_range')
        filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    else:
        selected_category = st.selectbox(f"Choisissez la catégorie de {filter_criterion}", df[filter_criterion].unique())
        filtered_df = df[df[filter_criterion] == selected_category]


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
    st.subheader(f"Graphique en toile d'araignée pour les moyennes des variables sélectionnées ({filter_criterion} : {selected_category if filter_criterion != 'age' else f'{age_range[0]} - {age_range[1]}'})")
    st.pyplot(fig)


def load_view():
    st.title('Visualisation')
    st.write(
    '''
    Ci dessous quelques visualisations intéressante
    ''')

    df_org = pd.read_csv('./src/assets/data/anxiety_attack_dataset.csv')
    df = pd.read_csv('./src/assets/data/clean_data.csv')
    df['occupation'] = df_org['Occupation']
    df['gender'] = df_org['Gender']
    df['smoking'] = df['smoking'].replace({False:'No', True:'Yes'})
    
    with st.expander('Visualiser les correlations'):
        correlations(df)
    with st.expander('visualiser les catégories'):
        categorial(df)
    with st.expander('visualiser les moyennes filtrées'):
        radar(df)