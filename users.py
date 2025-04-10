from src.models.database import Database

# with Database() as db:
#     print(db.execute('''
#         PRAGMA table_info(users);
#         ''', ()
#         ).fetchall())

with Database() as db:
    db.create_user_raffi()
