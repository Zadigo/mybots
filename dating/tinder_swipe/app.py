"""A bot that analyses Tinder images and determines
whether or not the girls are attractive by swiping
left or right
"""

import flask
from flask import Flask
from logic import CNNModel
import os
from settings import IMAGES, MEDIA_ROOT

app = Flask(__name__)

app.config['MODEL'] = CNNModel()

@app.route('/', methods=['GET'])
def index(*args, **kwargs):
    return flask.render_template('home/hero.html')

@app.route('/get-prediction', methods=['POST'])
def get_prediction(*args, **kwargs):
    prediction = app.config['MODEL'].do_prediction([[157]])
    return flask.jsonify(prediction=prediction)

@app.route('/get-image/<name>', methods=['GET'])
def get_image(*args, **kwargs):
    return flask.send_from_directory(os.path.join(MEDIA_ROOT, 'data', 'valid'), kwargs['name'])

@app.route('/get-images', methods=['GET'])
def get_images(*args, **kwargs):
    return flask.jsonify(images=IMAGES)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
