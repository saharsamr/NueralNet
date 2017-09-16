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

    def computeValue(self, activationFunc, parameter):
        self.activationFunc = activationFunc
        self.activationFuncParameter = parameter
        self.output = activationFunc.evalf(subs= {parameter: self.weights.dot(self.inputs.T)})

    def derivativeFunc(self, parameter):
        print 'derivativeFunc: ', self.activationFunc.diff(parameter)
        return self.activationFunc.diff(parameter)

    def partialDerivative(self):
        parameter = self.activationFuncParameter
        self.pDerivative = self.derivativeFunc(parameter).evalf(subs = {parameter: (self.weights.dot(self.inputs.T))})
        print 'partialDerivative: ', self.pDerivative
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
    y.computeValue(f(x), x)
    z = y.partialDerivative()
