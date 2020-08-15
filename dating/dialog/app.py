"""A bot that sends messages to tinder users automatically
by using Twilio, Google AutoDialog and ...
"""

import flask
from flask import Flask

app = Flask(__name__)

@app.route('/main', methods=['POST'])
def index(*args, **kwargs):
    pass

@app.route('/sms', methods=['POST'])
def sms(*args, **kwargs):
    pass

if __name__ == "__main__":
    app.run(port=5000, debug=True)
