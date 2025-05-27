import sys
sys.path.append("C:/GitHub/flask_project") 
from models.database import session
from models.user_model import User
from schemas.user_schema import users_schema

user = session.query(User).all()
res = users_schema.dump(user)
print(res)

print('===============================================\n')

import json
json_convert = json.dumps(res)
print(json_convert)