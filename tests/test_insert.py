import sys
sys.path.append("C:/GitHub/flask_project") 
from models.database import session
from models.user_model import User

new_user = User(name="John", email="john@example.com")
session.add(new_user)
session.commit()
session.refresh(new_user)

print("✅ User added successfully!")
session.close()