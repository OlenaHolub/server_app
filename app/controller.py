from flask import Flask
from flask_restful import Api

from .swap.controller import AiSwap
from .zip.controller import ZipCode


def app_server(config_filename):
    app = Flask(__name__, static_folder='static', template_folder='template')
    app.config.from_object(config_filename)
    api = Api(app)
    api.add_resource(ZipCode, '/code')
    api.add_resource(AiSwap, '/swap')
    return app
