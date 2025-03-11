from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate

app = Flask(__name__)
ma = Marshmallow(app)

class UserSchema(ma.Schema):
    name = fields.Str(required=True, validate = validate.Length(min=2, max=20)) # ✅ Corrected validation
    email = fields.Email(required=True) # ✅ Ensures it's a valid email

user_schema = UserSchema()


@app.route('/validate', methods = ['POST'])
def validate_user():
    data = request.get_json()
    error = user_schema.validate(data)

    if error:
        return jsonify(error), 404
    return jsonify({"message": "Validation successful!", "data": data}), 200


if __name__ == "__main__":
    app.run(debug=True)

