#!flask/bin/python

# API for getting current time
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to timeChecker"

@app.route('/api/time', methods=['GET'])
def get_current_time():
    now = datetime.now()
    current_time = now.isoformat(' ')
    return jsonify({'dateTime': current_time })


if __name__ == "__main__":
    app.run(debug="true", host="0.0.0.0")