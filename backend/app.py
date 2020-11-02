from flask import Flask
from flask_cors import CORS
from models import setup_db


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route("/")
    def index():
        return "Welcome to PasteIt API. This service is up and running."

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
