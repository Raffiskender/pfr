from src.models.database import Database
from src.models.session import Session
import pandas as pd

with Database() as db:
    db.execute('''
        CREATE TABLE IF NOT EXISTS patient(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            gender_is_male INTEGER,
            gender_is_female INTEGER,
            gender_is_other INTEGER)
    ''', ())
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS health(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            breathing_rate INTEGER,
            medication INTEGER,
            family_history INTEGER,
            sweating_level INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patient(id)
        );
    ''', ())

    db.execute('''
        CREATE TABLE IF NOT EXISTS life_style(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            job_is_Doctor INTEGER,
            job_is_Engineer INTEGER,
            job_is_Other INTEGER,
            job_is_Student INTEGER,
            job_is_Teacher INTEGER,
            job_is_Unemployed INTEGER,
            physical_activity INTEGER,
            sleed_hours INTEGER,
            caffeine_intake INTEGER,
            alcohol_consuption INTEGER,
            is_smoker INTEGER,
            diet_quality INTEGER,
            stress INTEGER,
            recently_chocked INTEGER,
            therapy_session INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patient(id)
        );
    ''', ())

    db.execute('''
        CREATE TABLE IF NOT EXISTS attack(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            heart_rate INTEGER,
            severity INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patient(id)
        );
    ''', ())

df = pd.read_csv("./data/clean_data.csv")

with Database() as db:
    for _, row in df.iterrows():
        cur = db.execute('''
            INSERT INTO patient (age, gender_is_male, gender_is_female, gender_is_other)
            VALUES (?, ?, ?, ?)
        ''', (row['age'], row['gender_Male'], row['gender_Female'], row['gender_Other']))

        patient_id = cur.lastrowid

        db.execute('''
            INSERT INTO health (patient_id, breathing_rate, medication, family_history, sweating_level)
            VALUES (?, ?, ?, ?, ?)
        ''', (patient_id, row['breathing_rate'], row['medication'], row['family_history'], row['sweating_level'])
        )

        db.execute('''
            INSERT INTO life_style (patient_id, job_is_Doctor, job_is_Engineer, job_is_Other, job_is_Student, job_is_Teacher, job_is_Unemployed, physical_activity, sleed_hours, caffeine_intake, alcohol_consuption, is_smoker, diet_quality, stress, recently_chocked, therapy_session)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (patient_id, row['occupation_Doctor'], row['occupation_Engineer'], row['occupation_Other'], row['occupation_Student'], row['occupation_Teacher'], row['occupation_Unemployed'], row['physical_activity'], row['sleep_hours'], row['caffeine_intake'], row['alcohol_consuption'], row['smoking'], row['diet_quality'], row['stress_level'], row['recent_life_event'], row['therapy_session'])
        )
        
        db.execute('''
            INSERT INTO attack (patient_id, heart_rate, severity)
            VALUES (?, ?, ?)
        ''', (patient_id, row['heart_rate_during_attack'], row['attack_severity'])
        )
    
    db.commit()