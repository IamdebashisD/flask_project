from flask import Blueprint, request, jsonify
from models.database import session
from models.user_model import User
from sqlalchemy.exc import SQLAlchemyError

delete_user_bp = Blueprint("delete_user_bp", __name__)

@delete_user_bp.route("/delete_user/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = session.query(User).filter_by(id=id).first()
    
    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        session.delete(user)
        session.commit()
        return jsonify({"message": "User deleted successfully!"}), 200
    
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of failure
        return jsonify({"error": "Internal Server Error"}), 500