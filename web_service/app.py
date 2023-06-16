from flask import Flask
from flask_cors import CORS
from .api import files


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 160 * 1000 * 1000

    app.register_blueprint(files.files_api, url_prefix="/api")
    cors_resources = {"/api/*": {"origins": "*"}}
    app.cors = CORS(app, resources=cors_resources)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
