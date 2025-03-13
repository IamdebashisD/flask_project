from flask import Blueprint, request, jsonify
from models.database import session
from models.user_model import User
from schemas.user_schema import user_schema
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

update_user_bp = Blueprint('/update_user_bp', __name__)
@update_user_bp.route('/update_user/<int:id>', methods=['PUT'])
def update_user(id):
    try:    
        with session.begin():
            user = session.query(User).filter_by(id=id).first()
            if not user:
                return jsonify({"error": "User not found"}), 404

            data = user_schema.load(request.json, partial=True)
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            session.commit()

        return jsonify({"Message": "User updated successfully!", "user": user_schema.dump(user)}), 200
    
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400  # Invalid input
    
    except SQLAlchemyError as err:
        session.rollback()  # Rollback if any database error occurs
        return jsonify({"error": "Internal Server Error"}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()




    
