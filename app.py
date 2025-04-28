from __init__ import create_app
from schemas.user_schema import ma

app = create_app()
ma.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

