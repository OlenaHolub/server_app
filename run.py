#!/usr/bin/env python

from flask import Flask
from flask_restful import Api

from app.swap.controller import AiSwap
from app.zip.controller import ZipCode


def app_server(config_filename):
    app = Flask(__name__, static_folder='static', template_folder='template')
    app.config.from_object(config_filename)
    api = Api(app)
    api.add_resource(ZipCode, '/code', endpoint='zip')
    api.add_resource(AiSwap, '/swap', endpoint='swap')
    return app


app = app_server('config')

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
