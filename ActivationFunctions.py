import numpy as np


class Sigmoid:
    name = "Sigmoid"
    _min = 0
    _max = 1

    def forward(self, x):
        return 1 / (1 + np.exp(-x))

    def backward(self, x):
        return x * (1 - x)

    def formatData(self, data):
        minValue = np.amin(data)
        maxValue = np.amax(data)

        return self._min * (data == minValue) + self._max * (data == maxValue)


class Elliott:
    name = "Elliott"
    _min = -1
    _max = 1

    def forward(self, x):
        return x / (1 + np.abs(x))

    def backward(self, x):
        xAbs = 1 + np.abs(x)
        return 1 / (xAbs * xAbs)

    def formatData(self, data):
        minValue = np.amin(data)
        maxValue = np.amax(data)

        return self._min * (data == minValue) + self._max * (data == maxValue)

class Tahn:
    name = "Tahn"
    _min = -1
    _max = 1

    def forward(self, x):
        return 2 / (1 + np.exp(-2 * x)) - 1

    def backward(self, x):
        return 1 - x * x

    def formatData(self, data):
        minValue = np.amin(data)
        maxValue = np.amax(data)

        return self._min * (data == minValue) + self._max * (data == maxValue)

class Step:
    name = "Step"
    _min = 0
    _max = 1

    def forward(self, x):
        return 1 * (x > 0)

    def backward(self, x):
        return 0.5 * (np.sign(x) + 1)

    def formatData(self, data):
        minValue = np.amin(data)
        maxValue = np.amax(data)

        return self._min * (data == minValue) + self._max * (data == maxValue)