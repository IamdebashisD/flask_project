from flask import Blueprint, request, jsonify, Response
from models.database import session
from models.user_model import User
from schemas.user_schema import user_schema
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from flasgger import swag_from
from flask_jwt_extended import jwt_required

update_user_bp = Blueprint('/update_user_bp', __name__)
@update_user_bp.route('/update_user/<string:id>', methods=['PUT'])
@swag_from('swagger/update_users.yml')  # must match exact file path
@jwt_required()
def update_user(id: str) -> Response:
    """Update an existing user"""
    try:    
        with session.begin():
            user: User | None = (
                session.query(User)                 
                .filter_by(id=id)
                .first()
            )

            if not user:
                return jsonify({"error_code": True, "error": "User not found", "data": None}), 404

            data = user_schema.load(request.json, partial=True)
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            session.commit()

            return jsonify({
                "error_code": False, 
                "message": "User updated successfully!", 
                "data": user_schema.dump(user)
                }), 200
    
    except ValidationError as err:
        return jsonify({"errors": err.messages, "data": None}), 400  # Invalid input
    
    except SQLAlchemyError as err:
        session.rollback()  # Rollback if any database error occurs
        return jsonify({"error": "Internal Server Error", "data": None}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500




    
