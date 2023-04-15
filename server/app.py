from flask import Flask, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Create the Swagger UI blueprint
# URL for exposing Swagger UI (without trailing '/')
SWAGGER_URL = '/swagger'

# URL for exposing OpenAPI spec (without trailing '/')
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Fmly Landing Page API"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()
