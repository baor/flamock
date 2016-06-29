import sys
import logging
from flask import Flask
from flask import request
from response_generator import ResponseGenerator

app = Flask(__name__)

flamock_admin_methods = ['add_expectation', 'get_expectations', 'remove_expectation', 'remove_all_expectations']

@app.route('/flamock/', defaults={'request_path': ''})
@app.route('/flamock/<path:request_path>')
def flamock_admin(request_path):
    #todo
    pass


@app.route('/', defaults={'request_path': ''})
@app.route('/<path:request_path>')
def hello_world(request_path):
    req = {'path': request_path, 'headers': request.headers, 'body': request.data, 'cookies': request.cookies}
    return ResponseGenerator(req).generate()


if __name__ == '__main__':
    app.run()
