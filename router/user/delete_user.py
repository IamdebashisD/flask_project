from flask import Blueprint, request, jsonify
from models.database import session
from models.user_model import User
from sqlalchemy.exc import SQLAlchemyError
from flasgger import swag_from
from flask_jwt_extended import jwt_required

delete_user_bp = Blueprint("delete_user_bp", __name__)

@delete_user_bp.route("/delete_user/<string:id>", methods=["DELETE"])
@swag_from('swagger/delete_user.yml')
@jwt_required()
def delete_user(id):
    '''Delete an existing user'''
    user: User | None = (session.query(User)
                        .filter_by(id=id)
                        .first())    
    
    if not user:
        return jsonify({"error": "User not found", "error_code": True}), 404
    
    try:
        session.delete(user)
        session.commit()
        return jsonify({"error_code": False, "message": "User deleted successfully!"}), 200
    
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of failure
        return jsonify({"error": "Internal Server Error"}), 500

    except Exception as e:
        print(str(e))
        return jsonify({"error":True, "message": str(e)})