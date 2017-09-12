import numpy as np
from sympy import Symbol
import math

class Neuron:
    def __init__(self,inputsNum):
        self.output = 0
        self.inputsNum = inputsNum
        self.weights = np.random.rand(1, self.inputsNum)
        self.inputs = np.random.rand(1, self.inputsNum)

    def computeValue(self, activationFunc):
        # self.output = activationFunc(self.weights, self.inputs)
        self.activationFunc = activationFunc
        d = activationFunc.diff('x')

if __name__ == "__main__":
    y = Neuron(2)
    x = Symbol('x')
    f = 1 /(1 + math.e**(-x))
    y.computeValue(f)
    print y
