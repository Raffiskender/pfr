from src.models.database import Database
from src.models.session import Session

import json 

with Database() as db:
    db.setup()

s = Session("raffi", "1234", "Raffi", 1, 1)
s.signin()

data = {      
    "email" : ""
}

with open("session.json", 'w') as outfile:
    json.dump(data, outfile)