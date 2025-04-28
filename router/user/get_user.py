from flask import Blueprint, request, jsonify, Response
from models.database import session
from models.user_model import User
from schemas.user_schema import users_schema
from sqlalchemy.exc import SQLAlchemyError
import logging
from flasgger import swag_from

get_user_bp = Blueprint('get_user_bp', __name__)
@get_user_bp.route('/get_users', methods=['GET'])
@swag_from('swagger/get_users.yml')
def get_user() -> Response:
    '''Fetch all user'''
    try:
        users = session.query(User).all()
        if not users:
            return jsonify({"message": "No users found", "users": []}), 200
        
        return jsonify({ 
            "status": "success", 
            "message": "Users fetched successfully", 
            "total_user": len(users),
            "data": users_schema.dump(users)
            }), 200
    
    except SQLAlchemyError as e:
        logging.error(f"Database Error: {str(e)}")  # Log error properly
        return jsonify({"error": "Internal Server Error"}), 500  # Secure error response
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500