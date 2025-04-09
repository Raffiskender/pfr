from src.models.database import Database

# with Database() as db:
#     print(db.execute('''
#         PRAGMA table_info(users);
#         ''', ()
#         ).fetchall())

with Database() as db:
    db.drop_users_table()
    db.setup_users_table()
    db.create_user_raffi()
