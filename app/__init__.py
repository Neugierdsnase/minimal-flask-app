import os

from flask import Flask
from .main import main as main_blueprint

# instantiate extensions here


def create_app(setting="default"):
    app = Flask(__name__)
    if setting == "default" or setting == "development":
        app.config["DEBUG"] = True
    elif setting == "production":
        app.config["DEBUG"] = False
    else:
        print("No valid configuration.")
        return False

    # initialize extensions here

    app.register_blueprint(main_blueprint)

    return app
