"""
Initializes the Flask application.
"""
from flask import Flask, jsonify
from calculator.models import db
from calculator.controllers.main import main


def create_app(object_name, env="prod"):
    """
    Creates flask app.
    Defines two custom error handlers.
    Initialize database.
    Registers blueprints for main module.
    """
    app = Flask(__name__)

    app.config.from_object(object_name)

    # define custom errors
    @app.errorhandler(400)
    def custom_error_400(error):
        response = jsonify({
            'code': 400,
            'message': 'Error 400 Bad request',
            'description': error.description,
        })
        response.status_code = 400
        return response

    @app.errorhandler(500)
    def custom_error_500(error):
        response = jsonify({
            'code': 500,
            'message': 'Error 500 Internal server error',
            'description': error.description,
        })
        response.status_code = 500
        return response

    db.init_app(app)

    app.register_blueprint(main)

    return app
