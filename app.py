from flask import Flask, request, render_template
import numpy as np
import json
import codecs
import os
import ActivationFunctions as af


app = Flask(__name__)
W0 = 0
W1 = 0
CONFIG = 0
activationFunction = 0
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognizer/', methods=['POST'])
def recognizer():
    sent_data = request.form['data']

    if len(sent_data) != 400:
        return 'Invalid request'

    sent_data += '1'
    formated = np.array(list(sent_data), dtype=np.int8)
    predicted = predict(formated)

    results =  str(np.argmax(predicted))
    for i in range(10):
        validNumber = round(((predicted[i] + 1) / 2), 4)
        results += "<p>" + str(i) + ": " + str(validNumber) + "</p>"

    return results

@app.route('/trainer/', methods=['POST'])
def train():
    sent_data = request.form['data']
    digit = request.form['digit']

    if len(sent_data) != 400 or not digit:
        return 'Invalid request'

    data_matrix = np.zeros(shape=(28,28), dtype=np.int8)
    for x in range(20):
        for y in range(20):
            data_matrix[x + 4, y + 4] = sent_data[x * 20 + y]

    array = data_matrix.reshape(-1).astype(np.int8) * 255
    dataFile = open('data.csv','ab')
    dataFile.write(digit + ",")
    array.tofile(dataFile,sep=',',format='%1.0f')
    dataFile.write("\n")
    dataFile.close()

    return "Added"

def predict(data):
    global W0, W1, activationFunction
    l1 = activationFunction.forward(np.dot(data, W0))
    l2 = (np.dot(l1, W1))

    return af.Activation().normalize(l2)

def loadWeights(weight0, weight1):
    global W0, W1
    W0 = importData(weight0)
    W1 = importData(weight1)

def importData(name):
    obj_text = codecs.open(os.path.join(APP_ROOT, name), 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    a_new = np.array(b_new, dtype=np.float32)
    return a_new

def setActivationFunction(x):
    x = x.lower()
    return {
        'sigmoid': af.Sigmoid(),
        'tahn': af.Tahn(),
        'elliott': af.Elliott(),
        'step': af.Step(),
    }.get(x, af.Sigmoid())

if __name__ == '__main__':
    global CONFIG, activationFunction
    with open(os.path.join(APP_ROOT, "config.json")) as fd:
        CONFIG = json.load(fd)

    activationFunction = setActivationFunction(CONFIG['activationFunction'])

    loadWeights(CONFIG['layer1'], CONFIG['layer2'])
    app.run(host='0.0.0.0', port=CONFIG['port'])