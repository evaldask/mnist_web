from flask import Flask, request, render_template
import numpy as np
import json
import codecs
import os


app = Flask(__name__)
W0 = 0
W1 = 0
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognizer/', methods=['GET', 'POST'])
def recognizer():
    sentData = request.form['data']

    if len(sentData) != 400:
        return 'Invalid request'

    sentData += '1'
    formated = np.array(list(sentData), dtype=np.float32)
    predicted = predict(formated)

    results =  str(np.argmax(predicted))
    for i in range(10):
        validNumber = round(((predicted[i] + 1) / 2), 4)
        results += "<p>" + str(i) + ": " + str(validNumber) + "</p>"

    return results

def predict(data):
    global W0
    l1 = sigmoid(np.dot(data, W0))
    global W1
    l2 = (np.dot(l1, W1))
    return tanFunc(l2)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanFunc(x):
    return np.tanh(x)

@app.before_first_request
def loadWeights():
    print "Weights have been loaded!"
    global W0
    W0 = importData("layer_1.json")
    global W1
    W1 = importData("layer_2.json")

def importData(name):
    obj_text = codecs.open(os.path.join(APP_ROOT, name), 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    a_new = np.array(b_new, dtype=np.float32)
    return a_new

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
