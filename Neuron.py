import numpy as np

class Neuron:
    def __init__(self,inputsNum):
        self.output = 0
        self.weights = np.random.rand(1, self.inputsNum)
        self.inputs = np.random.rand(1, self.inputsNum)

    def computeValue(self, activationFunc):
        self.output = activationFunc(self.weights, self.inputs)
