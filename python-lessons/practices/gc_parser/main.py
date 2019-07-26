# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request
from parser import parse
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = 'test123'


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/submit_log', methods=['POST'])
def submit_log():
    _file = request.files['file1']
    data = None
    if _file:
        file_name = secure_filename(_file.filename)
        file_name = os.path.join(app.config('UPLOAD_FOLDER'),file_name)
        _file.save(file_name)
        data = parse('SUN',file_name)
    print(data)
    if data:
        return render_template('result.html',data=data)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    print("running in Debug:%s mode"%app.config['DEBUG'])
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])

