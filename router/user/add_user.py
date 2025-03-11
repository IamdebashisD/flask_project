from flask import Blueprint, request, jsonify
from models.database import session
from models.user_model import User
from schemas.user_schema import user_schema
from marshmallow import ValidationError


# create a Blueprint for user creation
add_user_bp = Blueprint('add_user_bp', __name__)
@add_user_bp.route('/add_user', methods =['POST'])
def add_user():
    try:
        # Safely get JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid json data!"}), 404
        
        # Validate & deserialize input
        validate_data = user_schema.load(data)
        # create new user
        new_user = User(name=validate_data['name'], email = validate_data['email'])
        # Add user to session & commit
        session.add(new_user)
        session.commit()
        return jsonify({"message": "User added successfully!", "user": user_schema.dump(new_user)}), 201
    
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    
    except Exception as e:
        session.rollback() # Rollback in case of failure
        return jsonify({"error": str(e)}), 500
    
    finally:
        session.close()