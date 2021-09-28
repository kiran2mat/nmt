from flask import Flask
from flask.ext.cors import CORS, cross_origin
from flask import jsonify
from flask import request
import json
import os
import binascii
import cv2


app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

@app.route('/translate',methods = ['post'])
def hello():
    print(request.get_data())
    return jsonify("MeFFTUFCUJGYucoup")


@app.route('/upload',methods = ['post'])
def ocr():
    print(request.get_data())
    print(request.files)
    file = request.files['myFile']
    print(file)
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)
    
    return jsonify("Merci beaucoup")






if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=False)
    #app.run()
