from src.models.database import Database
import pandas as pd

with Database() as db:
    print(db.execute('''
        SELECT * FROM patient LIMIT 5
        ''', ()
        ).fetchall())
    
    print(db.execute('''
        SELECT * FROM health LIMIT 5
        ''', ()
        ).fetchall())
    
    print(db.execute('''
        SELECT * FROM life_style LIMIT 5
        ''', ()
        ).fetchall())
    
    print(db.execute('''
        SELECT * FROM attack LIMIT 5
        ''', ()
        ).fetchall())
    