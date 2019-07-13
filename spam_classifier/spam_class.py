# Import flask which will handle our communication with the frontend
# Also import few other libraries
from flask import Flask, render_template, request,jsonify
import numpy as np
import sys
import os
from joblib import dump,load
from sklearn.feature_extraction.text import CountVectorizer
from load import *


# Path to our saved model
# sys.path.append(os.path.abspath("./model"))
#clf = load('C:/Users/oscar/Desktop/project/How-to-Deploy-Keras-Models/flask_deploy/model/spamModel/spamPredict.joblib')
# Initialize flask app
#vectorizer = load('C:/Users/oscar/Desktop/project/How-to-Deploy-Keras-Models/flask_deploy/model/spamModel/vectroizer.pk1')
clf, vectorizer = init()
app = Flask(__name__)
#Initialize some global variables

# Separete the prefix of base64 of the content of image.

@app.route('/')
def index():
    return render_template("form.html")


@app.route('/spampr' ,methods=['GET', 'POST'])
def spampr():
    messaje = request.form['messaje']

    if messaje:
        print('ok')
        data= vectorizer.transform([str(messaje)])
        calculous= clf.predict(data)
        if str(calculous[0])== 'ham':
            return jsonify({'correct' : 'Non Spam'})
        else:
            return jsonify({'error' : 'Spam'})


if __name__ == "__main__": 
# run the app locally on the given port
    app.run(host='localhost', port=8000)
