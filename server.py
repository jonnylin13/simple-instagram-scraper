import api
from flask import Flask, jsonify

app = Flask('instascrap_server')
app.debug = True


@app.route('/')
def index():
    return '<p>Hello World</p>'


@app.route('/get_user/<string:username>', methods=['GET'])
def get_user(username):
    # For testing
    return jsonify(api.get_user(username)._user_data)


if __name__ == '__main__':
    app.run()
