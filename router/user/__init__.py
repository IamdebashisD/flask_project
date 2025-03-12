from flask import Blueprint
from .add_user import add_user_bp
from .get_user import get_user_bp
from .update_user import update_user_bp
from .delete_user import delete_user_bp

# Create a main blueprint for all user routes
user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

# Register all user_related blueprints inside user_bp
user_bp.register_blueprint(add_user_bp)
user_bp.register_blueprint(get_user_bp)
user_bp.register_blueprint(update_user_bp)
user_bp.register_blueprint(delete_user_bp)
