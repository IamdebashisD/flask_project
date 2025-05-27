# services/user_services.py
from models.database import session
from models.user_model import User
from sqlalchemy.exc import SQLAlchemyError

def get_all_users():
    try:
        users = session.query(User).all()
        return users
    except SQLAlchemyError as e:
        print(f"Error fetching users: {e}")
        return []

def get_user_by_id(user_id: str):
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    except SQLAlchemyError as e:
        print(f"Error fetching user by ID: {e}")
        return None

all_users = get_all_users()
for user in all_users:
    print(f'id: {user.id} name: {user.name}     email: {user.email}')