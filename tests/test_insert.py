import sys
sys.path.append("C:/GitHub/flask_project") 
from models.database import session
from models.user_model import User
from schemas.user_schema import user_schema

user = session.query(User).all()
res = user_schema.dump(user)
print(res)