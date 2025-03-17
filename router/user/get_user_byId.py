from flask import Blueprint, jsonify, Response
from models.database import session
from models.user_model import User
from schemas.user_schema import user_schema
from sqlalchemy.exc import SQLAlchemyError
import logging

get_user_byId_bp = Blueprint('get_user_byId', __name__)
@get_user_byId_bp.route('/get_user_byId/<int:id>', methods= ['GET'])
def get_user_byId(id) -> Response:
    """Fetch a user by ID"""
    try:
        user: User | None = session.query(User).filter_by(id=id).first()
        if not user:
            return jsonify({'Msg': "User not found!"}), 404
        return jsonify({
            "status":"success", 
            "msg": "User fetch successfully!",
            "data": user_schema.dump(user)
        }), 200
    
    except SQLAlchemyError as SQlerror:
        logging.error(f"database error {str(SQlerror)}")
        return jsonify({"error": "Internal Server Error"}), 500
    
    except Exception as e: return jsonify({"error": str(e)}), 500


