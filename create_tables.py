from models.database import engine, Base
from models.user_model import User  # ⚡ Required! Ensures SQLAlchemy registers the model

# ✅ Create all tables

Base.metadata.create_all(engine)

print("✅ Tables created successfully!")


