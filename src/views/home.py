import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load():

    st.title("Crises d'anxiété")

    st.markdown(
    """
    Cette appli présente un jeu de donnée sur l'anxiété, et permet de visualiser les données, les analyser et éventuellement les interpréter.
    Les données sont issues de Kaggle. Bien que n'étant plus disponibles sur la plateforme, les données brutes sont disponibles <a class="link" href="https://drive.google.com/drive/folders/11vW2AomLorVeJd3xdR83bEynd7gCxIsU?usp=drive_link" target="_self">sur mon google drive personnel</a>.

    Sur cette page vous aurez :

    * [La présentation des données](#693dc7ba)
    * [Les objectifs](#objectifs)
    * [Des visuels de répartition](#e4c37833)
    * [les objectifs](#les-objectifs)

    """, unsafe_allow_html=True)

    st.header("Présentation des données")
    
    st.markdown(
    """
    Ci dessous un extrait du dataframe. Plus de détail sur ces données <a class="link" href="/cleaning" target="_self">ici</a>

    """, unsafe_allow_html=True)

    df = pd.read_csv('./src/assets/data/clean_data.csv')
    with st.expander("Afficher les premières lignes"):
        st.dataframe(df.head(5))

    st.markdown(
    f"""
    ## Visuels de répartitions
    
    Ci-dessous une analyse rapide de la répartition des données. Une analyse plus approfondie sur <a class="link" href="/?page=eda" target="_self">cette page</a>
    """, unsafe_allow_html=True)
    
    # df données pour les graphiques :
    
    #Les genres
    df_gender = df[['gender_Female', 'gender_Male', 'gender_Other']].sum()
    #Le travail
    df_job = df[['occupation_Doctor', 'occupation_Engineer', 'occupation_Other', 'occupation_Student', 'occupation_Teacher', 'occupation_Unemployed']].sum()

    #Les ages
    age_tranches = ((11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70))
    df_age = pd.DataFrame()
    for tranche in age_tranches:
        df_age[f'{tranche[0]}-{tranche[1]}'] = [df['age'][(tranche[0] < df['age']) & (df['age'] < tranche[1])].count()]
    
    df_age = df_age.melt(var_name='Age Range', value_name='count')
    
    #Les fumeurs
    df_smokers = pd.DataFrame(
        {'count':[
            df[['smoking']].sum(),
            df.shape[0] - df[['smoking']].sum()
        ]},
        index=['Smoker', 'Non smoker'])

    fig, axes = plt.subplots(5, 2, figsize=(10, 15))

    plt.rcParams.update({'font.size':   11,    # Taille des titres des axes
                     'axes.labelsize':  11,          # Taille des labels des axes
                     'xtick.labelsize': 11,         # Taille des labels des ticks X
                     'ytick.labelsize': 11,         # Taille des labels des ticks Y
                     'legend.fontsize': 11})        # Taille de la légende

    plt.subplots_adjust(hspace=1, wspace=0.5)

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
    
    # Répartition des genres
    
    axes[0, 0].set_title("Répartition des genres")
    labels = ['Female', 'Male', 'Other']
    axes[0, 0].pie(df_gender, labels=labels, colors=colors, autopct='%1.1f%%')

    # Répartition du travail
    axes[0, 1].set_title("Répartition du travail")
    labels = ['Doctors', 'Engineers', 'Others', 'Students', 'Teachers', 'Unemployed']
    axes[0, 1].pie(df_job, labels=labels, colors=colors, autopct='%1.1f%%')
   
    # Répartition des ages
    axes[1, 0].set_title("Répartition des ages")
    labels = ['11-20', '21-30', '31-40', '41-50', '51-60', '61-70']
    axes[1, 0].pie(df_age['count'], labels=labels, colors=colors, autopct='%1.1f%%')
    
    # Répartition des fumeurs
    axes[1, 1].set_title("Répartition des fumeurs")
    labels = ['Fumeurs', 'Non fumeurs']
    axes[1, 1].pie(df_smokers['count'], labels=labels, colors=colors, autopct='%1.1f%%')


    #heures de someil :
    axes[2, 0].set_title("Répartition des heures de sommeil")
    axes[2, 0].text(0.8, 0.2, f'min : {df['sleep_hours'].min()}\n max : {df['sleep_hours'].max()}\n moy : {round(df['sleep_hours'].mean(), 2)}', ha='center', va='center', 
                transform=axes[2, 0].transAxes, fontsize=10, alpha=0.9, color='black')
    axes[2, 0].hist(df['sleep_hours'], bins=7, edgecolor='white')

    #activités phy
    axes[2, 1].set_title("Répartition des activités physiques")
    axes[2, 1].text(0.8, 0.2, f'min : {df['physical_activity'].min()}\n max : {df['physical_activity'].max()}\n moy : {round(df['physical_activity'].mean(), 2)}', ha='center', va='center', 
                transform=axes[2, 1].transAxes, fontsize=10, alpha=0.9, color='black')
    axes[2, 1].hist(df['physical_activity'], bins=10, edgecolor='white')

    #caféine intake
    axes[3, 0].set_title("Répartition de la conso de café (mg/jour)")
    axes[3, 0].text(0.8, 0.2, f'min : {df['caffeine_intake'].min()}\n max : {df['caffeine_intake'].max()}\n moy : {round(df['caffeine_intake'].mean(), 2)}', ha='center', va='center', 
                transform=axes[3, 0].transAxes, fontsize=10, alpha=0.9, color='black')
    axes[3, 0].hist(df['caffeine_intake'], bins=25, edgecolor='white')

    #conso alcool
    axes[3, 1].set_title("Répartition de la conso d'alcool (verre/semaine)")
    axes[3, 1].text(0.8, 0.2, f'min : {df['alcohol_consuption'].min()}\n max : {df['alcohol_consuption'].max()}\n moy : {round(df['alcohol_consuption'].mean(), 2)}', ha='center', va='center', 
                transform=axes[3, 1].transAxes, fontsize=10, alpha=0.9, color='black')
    axes[3, 1].hist(df['alcohol_consuption'], bins=20, edgecolor='white')

    # Répartition du sucre
    axes[4, 0].set_title("Répartition du sucre")
    axes[4, 0].text(0.8, 0.2, f'min : {df['sweating_level'].min()}\n max : {df['sweating_level'].max()}\n moy : {round(df['sweating_level'].mean(), 2)}', ha='center', va='center', 
                transform=axes[4, 0].transAxes, fontsize=10, alpha=0.9, color='black')
    axes[4, 0].hist(df['sweating_level'], edgecolor='white', bins=5)
    
    #répartition de l'alimentation
    axes[4, 1].set_title("Répartition de l'alimentation")
    axes[4, 1].text(0.8, 0.2, f'min : {df['diet_quality'].min()}\n max : {df['diet_quality'].max()}\n moy : {round(df['diet_quality'].mean(), 2)}', ha='center', va='center', 
                transform=axes[4, 1].transAxes, fontsize=10, alpha=0.9, color='black')
    axes[4, 1].hist(df['diet_quality'], edgecolor='white', bins=10)


# family_history,stress_level,dizziness,medication,therapy_session,recent_life_event,diet_quality,attack_severity


    plt.tight_layout()
    st.pyplot(fig)


    st.markdown(
    f"""
    On remarque en un coup d'oeil que les données semblent être correctement réparties et qu'il n'y pas de valeurs incohérentes ou aberrantes.

    ## Les objectifs
    
    """)

    st.subheader("1. Nettoyage des données")
    st.write("""
    Avant toute analyse, les données doivent être nettoyées.
    Au programme de cette étape : 
    - **Traitement des valeurs manquantes** : Remplir, imputer ou supprimer les valeurs manquantes en fonction du contexte.
    - **Correction des incohérences** : Identifier et rectifier les erreurs de saisie ou les doublons.
    - **Normalisation et transformation des données** : Mise à l'échelle des variables, conversion des formats de données, et agrégation des données si nécessaire.
    """)

    # 2. EDA & Analyse descriptive
    st.subheader("2. EDA & Analyse descriptive")
    st.write("""
    L'Exploratory Data Analysis (EDA) permet d'explorer la structure des données et de 
    mieux comprendre leurs caractéristiques statistiques.
    * Calcul des statistiques de base (moyenne, médiane, écart-type, etc.).
    * Identification des distributions des variables.
    * Calcul des **corrélations** entre variables pour identifier les relations potentielles.
    """)
  
    # 3. Visualisation des données
    st.subheader("3. Visualisation des données")
    st.write("""
    Les visualisations permettent de mieux comprendre les tendances et les relations dans les données. 
    Nous utiliserons des graphiques adaptés comme les histogrammes, les nuages de points et les heatmaps pour représenter les corrélations.
    """)

    # 4. Conclusions
    st.subheader("4. Conclusions")
    st.markdown("""
    À la fin du projet, nous résumerons les principaux enseignements tirés des analyses. 
    Ces conclusions permettront de proposer des recommandations pour améliorer la prise de décision et guider les actions futures.
    
    Mais pour voir tout çà il faut <a class="link" href="/?page=login" target="_self">vous connecter</a> ou <a class="link" href="/?page=signup" target="_self">créer un compte</a>.

    """, unsafe_allow_html=True)