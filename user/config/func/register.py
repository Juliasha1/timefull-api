from flasgger import Swagger

from packages.exports import *
from user.api.index import user_bp

def register_blueprints(app):
    app.register_blueprint(user_bp)
    # packages
    app.register_blueprint(task_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(form_bp)
    app.register_blueprint(timer_bp)




    





def register_swagger(app):
    SWAGGER_TEMPLATE = {
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "\JWT access token"
            }
        }
    }
    swag = Swagger(app, template=SWAGGER_TEMPLATE)
    app.config["SWAGGER"] = {
        "openapi": "3.0.0",
        "title": "Daytime api",
        "description": ""
    }