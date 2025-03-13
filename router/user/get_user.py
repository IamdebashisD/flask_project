from flask import Blueprint, request, jsonify
from models.database import session
from models.user_model import User
from schemas.user_schema import user_schema
from sqlalchemy.exc import SQLAlchemyError
import logging

get_user_bp = Blueprint('get_user_bp', __name__)
@get_user_bp.route('/get_user', methods=['GET'])
def get_user():
    try:
        users = session.query(User).all()
        if not users:
            return jsonify({"message": "No users found", "users": []}), 200
        return jsonify(user_schema.dump({"data": users})), 200
    
    except SQLAlchemyError as e:
        logging.error(f"Database Error: {str(e)}")  # Log error properly
        return jsonify({"error": "Internal Server Error"}), 500  # Secure error response
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500