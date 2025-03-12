from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, ValidationError

app = Flask(__name__)
ma = Marshmallow(app)

class UserSchema(ma.Schema):
    name = fields.Str(required=True, validate = validate.Length(min=2, max=20)) # Corrected validation
    email = fields.Email(required=True) # Ensures it's a valid email

user_schema = UserSchema(many=True)


@app.route('/validate', methods = ['POST'])
def validate_user():
    try:
        data = request.get_json()
        error = user_schema.load(data)
        if error:
            return jsonify(error), 404
        return jsonify({"message": "Validation successful!", "data": data}), 200
    
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400 