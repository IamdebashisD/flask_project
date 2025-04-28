from flask import Blueprint, jsonify, Response
from models.database import session
from models.user_model import User
from schemas.user_schema import user_schema
from sqlalchemy.exc import SQLAlchemyError
import logging
from flasgger import swag_from

get_user_byId_bp = Blueprint('get_user_byId_bp', __name__)
@get_user_byId_bp.route('/get_user_byId/<string:id>', methods= ['GET'])
@swag_from('swagger/get_user_by_id.yml')
def get_user_byId(id) -> Response:
    """Fetch a user by ID"""
    try:
        user: User | None = session.query(User).filter_by(id=id).first()

        if not user:
            return jsonify({'error_code': True, 'Msg': "User not found!"}), 404
        
        return jsonify({
            "error_code": False,
            "msg": "User fetch successfully!",
            "data": user_schema.dump(user)
        }), 200
    
    except SQLAlchemyError as SQlerror:
        logging.error(f"database error {str(SQlerror)}")
        return jsonify({"error": "Internal Server Error", "data": None}), 500
    
    except Exception as e: return jsonify({
        "message":"Internal server error!",
        "error": str(e),
        "data": None
        }), 500


