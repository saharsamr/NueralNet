import numpy as np
from sympy import Symbol
import math

class Neuron:
    def __init__(self,inputsNum):
        self.output = 0
        self.inputsNum = inputsNum
        self.weights = np.array(np.random.rand(1, self.inputsNum))
        self.inputs = np.array(np.random.rand(1, self.inputsNum))
        self.dWs = np.zeros(self.inputsNum)

    def computeValue(self, activationFunc):
        self.activationFunc = activationFunc
        self.output = activationFunc(self.weights.dot(self.inputs.T))

    def derivativeFunc(self, x):
        print sympy.diff(self.activationFunc(x), x)
        return sympy.diff(self.activationFunc(x), x)

    def partialDerivative(self):
        self.pDerivative = self.derivativeFunc(x).evalf(subs = {x: (self.weights.dot(self.inputs))})
        print self.pDerivative
        return self.pDerivative

    def setDerivative(self, weightIndex, dW):
        self.dWs[weightIndex] = dW

    def getdW(self, weightIndex):
        return self.dWs[weightIndex]

    def getW(self, weightIndex):
        return self.weights[weightIndex]

def f(x):
    return 1 /(1 + math.e**(-x))

if __name__ == "__main__":
    y = Neuron(2)
    x = Symbol('x')
    # f = 1 /(1 + math.e**(-x))
    y.computeValue(f(x))
    z = y.partialDerivative()
