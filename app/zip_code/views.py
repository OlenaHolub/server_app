import requests
from flask import Flask
from flask_restful import reqparse, Api, Resource

parser = reqparse.RequestParser()
parser.add_argument('code')


def app_zip(config_filename):
    app = Flask(__name__, static_folder='templates/static')
    app.config.from_object(config_filename)
    api = Api(app)

    class ZipCode(Resource):

        def post(self):
            args = parser.parse_args()
            address = args['code']
            key = 'AIzaSyDAIPtIC3Q6VE8PPQtKR9i_B8nSvZc5lB0'
            response = requests.get(
                'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + key)

            resp_json_payload = response.json()

            return resp_json_payload['results'][0]['geometry']['location']

    api.add_resource(ZipCode, '/code')

    return app
