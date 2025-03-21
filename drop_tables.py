from src.models.database import Database

with Database() as db:
    db.drop()