from flask_marshmallow import Marshmallow
from marshmallow import fields, validate

ma: Marshmallow = Marshmallow()

class UserSchema(ma.Schema):
    name = fields.Str(required=True, validate = validate.Length(min=2, max=20)) # Corrected validation
    email = fields.Email(required=True) # Ensures it's a valid email

# Created two instances of user schema 
user_schema: UserSchema = UserSchema() # Default is for a single user
users_schema: UserSchema = UserSchema(many=True) # Correct way to handle multiple users

