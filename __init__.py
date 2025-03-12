from flask import Flask
from models.database import Base, engine
from router.user import user_bp



def create_app():
    app = Flask(__name__)

    Base.metadata.create_all(engine)

    app.register_blueprint(user_bp) 
    
    return app
