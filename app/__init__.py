from flask import Flask


def create_app(config_filename):
    app = Flask(__name__, static_folder='templates/static')
    app.config.from_object(config_filename)

    @app.route('/')
    def index():
        return 'Hello World!'

    return app
