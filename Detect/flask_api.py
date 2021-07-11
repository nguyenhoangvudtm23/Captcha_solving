from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from yolov4_tiny_model import *
from gevent.pywsgi import WSGIServer

# define a flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # get the file from the post request
        f = request.files['file']

        # save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        result = detect_image(image_path=file_path)
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
