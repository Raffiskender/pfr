from src.models.data_model import DataModel
# from src.models.session import Session
import pandas as pd

df = pd.read_csv("./src/assets/data/clean_data.csv")

with DataModel() as db:
    db.drop_tables()
    db.setup_tables()
    db.fill_tables(df)