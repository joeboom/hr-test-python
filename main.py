from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/timestamp")
def get_timestamp():

    ts = datetime.timestamp(datetime.now())
    ts_int = int(ts)

    timestamp_data = {
        'timestamp': ts_int
    }

    return jsonify(timestamp_data), 200

@app.route("/readdata", methods = ['POST'])
def create_user():
    user_data = {
        'username': request.json['username'],
        'password': request.json['password']
    }

    return jsonify(user_data), 201

@app.errorhandler(404)
def invalid_route(e):
    return jsonify('404 Not Found')

if __name__ == "__main__":
    app.run(debug=True) 