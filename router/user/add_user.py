from flask import Blueprint, request, jsonify, Response
from models.database import session
from models.user_model import User
from schemas.user_schema import user_schema
from marshmallow import ValidationError
from flasgger import swag_from


# create a Blueprint for user creation
add_user_bp = Blueprint('add_user_bp', __name__)
@add_user_bp.route('/add_user', methods =['POST'])
@swag_from('swagger/add_user.yml')
def add_user() -> Response:
    """Creates a new user"""
    try:
        # Safely get JSON data
        data: dict = request.get_json()
        if not data:
            return jsonify({"error_code": True, "message": "Invalid JSON data!", "data": None}), 400
        
        # Validate & deserialize input
        validate_data = user_schema.load(data)

        # Check if email already exists
        existing_user = session.query(User).filter(User.email == validate_data['email']).first()
        if existing_user:
            return jsonify({"error_code": True, "message": "Email already exist!", "data": None}), 409

        # create new user
        new_user = User(name = validate_data['name'], email = validate_data['email'])
        print('>>>>>>>1>>>>>>>',new_user.name)
        # Add user to session & commit
        session.add(new_user)
        session.commit()

        return jsonify({
            "error_code": False, 
            "Mmessagee": "User added successfully!",
            "data": user_schema.dump(new_user)
        }), 201
        
    except ValidationError as err: return jsonify({
            "error_code": True, 
            "message": "Validation error", 
            "errors": err.messages, 
            "data": None
        }), 400
    
    except Exception as e:
        session.rollback() # Rollback in case of failure
        return jsonify({
            "error_code": True,
            "message": "Internal server error",
            "error": str(e)
        }), 500
    
    finally:
        session.close()