from flask import Flask, request, jsonify
from models.database import Base, engine
from router.user import user_bp
from flasgger import Swagger
import logging
import os
from colorlog import ColoredFormatter
from werkzeug.exceptions import HTTPException

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True
        }
    ],
    "static_url_path": "/static",
    "static_folder": "swagger",
    "swagger_ui": True,
    "specs_route": "/docs/" 
}

def create_app():
    app = Flask(__name__)

    Swagger(app, config=swagger_config, template={
        "swagger": "2.0",
        "info": {
            "title": "User API",
            "description": "API for managing users",
            "version": "1.0"
        },
        "consumes": ["application/json"],
        "produces": ["application/json"],
    })

    Base.metadata.create_all(engine)

    # ========== 🎨 Logger Setup with colorlog ==========
    logger = logging.getLogger()
    handler = logging.StreamHandler()

    formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s [%(asctime)s] %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    }
)

    handler.setFormatter(formatter)
    logger.handlers = []  # Clear existing handlers
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Suppress default werkzeug logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    # ===================================================

    # Fake process ID (optional)
    process_id = os.getpid()
    logger.info(f"Started server process [{process_id}]")
    logger.info("Waiting for application startup.")
    logger.info("Application startup complete.")
    logger.info("Logging running on http://127.0.0.1:5000")

    server_port = 5000

    @app.before_request
    def log_request_info():
        logger.info(f'{request.remote_addr}:{server_port} - "{request.method} {request.path} HTTP/1.1"')

    @app.after_request
    def log_response_info(response):
        logger.info(f'{request.remote_addr}:{server_port} - "{request.method} {request.path} HTTP/1.1" {response.status}')
        return response

    # ========== Custom Error Handler ==========
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Custom error handler to log errors and return a JSON response."""
        # Log error details in the terminal (mimicking FastAPI behavior)
        logger.error(f"{request.remote_addr} - \"{request.method} {request.path} HTTP/1.1\" {e.code} {e.name}")

        # Return custom error response for validation
        response = {
            "detail": [
                {
                    "loc": ["body", "field_name"],  # This should match your validation location
                    "msg": str(e),  # The error message (could be validation issue)
                    "type": "value_error.invalid"  # Custom error type
                }
            ]
        }
        
        # If the error is related to bad data, return a 400 or 422 status code
        return jsonify(response), e.code

    # Register your blueprints
    app.register_blueprint(user_bp) 

    return app
