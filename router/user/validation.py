from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from schemas.user_schema import user_schema
from flasgger import swag_from

validate_bp = Blueprint('/validate_bp', __name__)
@validate_bp.route('/validate', methods = ['POST'])
@swag_from('swagger/validate_user.yml')
def validate_user():
    try:
        data = request.get_json()

        validated = user_schema.load(data)

        return jsonify({
                "error_code": False,
                "message": "Validation successful!",
                "data": validated
        }), 200
    
    except ValidationError as err:
        return jsonify({
            "error_code": True,
            "message": "Validation failed!",
            "data": None,
            "error": err.messages
    }), 400
    except Exception as e:
        return({"message": str(e)})

