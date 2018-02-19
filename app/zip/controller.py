import requests
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('code')


class ZipCode(Resource):
    def post(self):
        args = parser.parse_args()
        address = args['code']
        key = 'AIzaSyDAIPtIC3Q6VE8PPQtKR9i_B8nSvZc5lB0'
        response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + key)

        resp_json = response.json()

        return resp_json['results'][0]['geometry']['location']
