import json
import os
from datetime import datetime

import apiai
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('question')


def log_question_answer(path, question, answer):
    if not os.path.exists(path):
        os.mkdir(path)
    pair = {'question': question, 'answer': answer}
    result = json.dumps({str(datetime.today().time()): pair})
    file_path = path + '/' + str(datetime.today().date()) + '.txt'
    with open(file_path, 'a') as file:
        file.write(result + '\n')


class AiSwap(Resource):
    def post(self):
        args = parser.parse_args()
        question = args['question']
        access_token = 'b8239c9a4739476abfc3f858b3cf8c0b'
        client = apiai.ApiAI(access_token)
        request = client.text_request()
        request.query = question
        byte_response = request.getresponse().read()
        json_response = byte_response.decode('utf8').replace("'", '"')
        response = json.loads(json_response)
        answer_response = response['result']['fulfillment']['speech']
        log_question_answer('logs', question, answer_response)
        return answer_response, 200
