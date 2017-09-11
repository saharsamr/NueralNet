import numpy as np

class Neuron:
    def __init__(self,inputsNum):
        self.outPut = 0
        self.weights = np.random.rand(1, self.inputsNum)
        self.inputs = np.random.rand(1, self.inputsNum)
