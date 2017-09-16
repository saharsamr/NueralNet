import numpy as np
import math
from sympy import Symbol

class NeuralNet:
    def __init__(self, layesNeuronNum, activationFunc):
        self.layesNeuronNum = layesNeuronNum
        self.activationFunc =activationFunc
        self.createNodes()
        self.createWeights()

    def createNodes(self):
        
