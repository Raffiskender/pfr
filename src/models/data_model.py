from src.models.database import Database
import pandas as pd
class DataModel(Database):
    def __init__(self):
        super().__init__()
        self.tables = ["patient", "health", "life_style", "attack"]

    def setup_tables(self):
        self.execute(
        '''
            CREATE TABLE IF NOT EXISTS patient(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                age INTEGER,
                gender_is_male INTEGER,
                gender_is_female INTEGER,
                gender_is_other INTEGER)
        ''', ())

        self.execute(
        '''
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

        self.execute(
        '''
            CREATE TABLE IF NOT EXISTS life_style(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                job_is_doctor INTEGER,
                job_is_engineer INTEGER,
                job_is_student INTEGER,
                job_is_teacher INTEGER,
                job_is_unemployed INTEGER,
                job_is_other INTEGER,
                physical_activity INTEGER,
                sleep_hours INTEGER,
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

        self.execute(
        '''
            CREATE TABLE IF NOT EXISTS attack(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                heart_rate INTEGER,
                dizziness INTEGER,
                severity INTEGER,
                FOREIGN KEY (patient_id) REFERENCES patient(id)
            );
        ''', ())

        self.commit()
        print('tables created')
        print(self.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
    
    def drop_tables(self):
        for table in self.tables:
            self.execute(f"DROP TABLE IF EXISTS {table}")
        self.commit()

    def fill_tables(self, df):
        for _, row in df.iterrows():
            cur = self.execute('''
            INSERT INTO patient (age, gender_is_male, gender_is_female, gender_is_other)
            VALUES (?, ?, ?, ?)
            ''', (row['age'], row['gender_Male'], row['gender_Female'], row['gender_Other']))

            patient_id = cur.lastrowid

            self.execute('''
                INSERT INTO health (patient_id, breathing_rate, medication, family_history, sweating_level)
                VALUES (?, ?, ?, ?, ?)
            ''', (patient_id, row['breathing_rate'], row['medication'], row['family_history'], row['sweating_level'])
            )

            self.execute('''
                INSERT INTO life_style (patient_id, job_is_doctor, job_is_engineer, job_is_other, job_is_student, job_is_teacher, job_is_unemployed, physical_activity, sleep_hours, caffeine_intake, alcohol_consuption, is_smoker, diet_quality, stress, recently_chocked, therapy_session)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (patient_id, row['occupation_Doctor'], row['occupation_Engineer'], row['occupation_Other'], row['occupation_Student'], row['occupation_Teacher'], row['occupation_Unemployed'], row['physical_activity'], row['sleep_hours'], row['caffeine_intake'], row['alcohol_consuption'], row['smoking'], row['diet_quality'], row['stress_level'], row['recent_life_event'], row['therapy_session'])
            )
            
            self.execute('''
                INSERT INTO attack (patient_id, heart_rate, dizziness,severity)
                VALUES (?, ?, ?, ?)
            ''', (patient_id, row['heart_rate_during_attack'], row['dizziness'], row['attack_severity'])
            )
        self.commit()
        print("Tables filled :")
        for table in self.tables:
            print(f"Table {table} : ")
            print(f"{self.execute(f"SELECT * FROM {table} LIMIT 5").fetchall()}...")

    def create_dataframe(self):
        with self as db:
            df = pd.read_sql(
            """
                SELECT patient.age, patient.gender_is_male, patient.gender_is_female, patient.gender_is_other,
                    health.breathing_rate, health.medication, health.family_history, health.sweating_level,
                    life_style.job_is_doctor, life_style.job_is_engineer, life_style.job_is_student, life_style.job_is_teacher, life_style.job_is_unemployed, life_style.job_is_other, life_style.physical_activity, life_style.sleep_hours, life_style.caffeine_intake, life_style.alcohol_consuption, life_style.is_smoker, life_style.diet_quality, life_style.stress, life_style.recently_chocked, life_style.therapy_session,
                    attack.heart_rate, attack.dizziness, attack.severity
                FROM patient
                JOIN health ON health.patient_id = patient.id 
                JOIN life_style ON life_style.patient_id = patient.id 
                JOIN attack ON attack.patient_id = patient.id 
            """, db.get_connection())            
        return df
    
    def fetchall(self):
        return self.execute(
        """
            SELECT patient.age, patient.gender_is_male, patient.gender_is_female, patient.gender_is_other,
                health.breathing_rate, health.medication, health.family_history, health.sweating_level,
                life_style.job_is_doctor, life_style.job_is_engineer, life_style.job_is_student, life_style.job_is_teacher, life_style.job_is_unemployed, life_style.job_is_other, life_style.physical_activity, life_style.sleep_hours, life_style.caffeine_intake, life_style.alcohol_consuption, life_style.is_smoker, life_style.diet_quality, life_style.stress, life_style.recently_chocked, life_style.therapy_session,
                attack.heart_rate, attack.dizziness, attack.severity
            FROM patient
            JOIN health ON health.patient_id = patient.id 
            JOIN life_style ON life_style.patient_id = patient.id 
            JOIN attack ON attack.patient_id = patient.id 
        """).fetchall()

    def fetchall_patient(self):
        data_dict = {'age':[], 'gender_is_male':[], 'gender_is_female':[], 'gender_is_other':[]}
        data = self.execute(f"SELECT age, gender_is_male, gender_is_female, gender_is_other FROM patient;").fetchall()
        
        for age, gender_is_male, gender_is_female, gender_is_other in data:
            data_dict['age'].append(age)
            data_dict['gender_is_male'].append(gender_is_male)
            data_dict['gender_is_female'].append(gender_is_female)
            data_dict['gender_is_other'].append(gender_is_other)
        return data_dict
    
    def fetchall_health(self):
        data_dict = {'breathing_rate':[], 'medication':[], 'family_history':[] ,'sweating_level':[]}
        data = self.execute("SELECT breathing_rate, medication, family_history, sweating_level FROM health").fetchall()

        for a, b, c, d in data:
            data_dict['breathing_rate'].append(a)
            data_dict['medication'].append(b)
            data_dict['family_history'].append(c)
            data_dict['sweating_level'].append(d)
        return data_dict
