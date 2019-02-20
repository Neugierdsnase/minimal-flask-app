import os

from flask import Flask
from .main import main as main_blueprint
from flask_misaka import Misaka

md = Misaka()


def create_app(setting="default"):
    app = Flask(__name__)
    if setting == "default" or setting == "development":
        app.config["DEBUG"] = True
        app.config["NUCLEAR_CODES"] = "insecure string"
    elif setting == "production":
        app.config["DEBUG"] = False
        app.config["NUCLEAR_CODES"] = os.environ.get("NUCLEAR_CODES")
    else:
        print("No valid configuration.")
        return False

    md.init_app(app)

    app.register_blueprint(main_blueprint)

    return app
