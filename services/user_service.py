from models.database import session
from models.user_model import User

query = session.query(User).all()
for user in query:
    print(f"{user.id} | {user.name} | {user.email}")