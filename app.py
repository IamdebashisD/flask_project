from __init__ import create_app
from schemas.user_schema import ma
from flask_jwt_extended import JWTManager
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()
ma.init_app(app)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=10)

if __name__ == '__main__':
    app.run(debug=True)

