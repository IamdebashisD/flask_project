from models.database import session
from models.user_model import User

users = session.query(User).all()

for user in users:
    print(f'name -> {user.name}, email -> {user.email}')
