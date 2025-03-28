from src.models.database import Database
from src.models.session import Session

with Database() as db:
    db.setup()

s = Session("raffi", "1234", "Raffi", 1, 1)
s.signin()

data = {      
    "email" : ""
}
