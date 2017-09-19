import numpy as np
from Neuron import Neuron
from keras.datasets import mnist
from sympy import Symbol
import math

class NeuralNet:
    def __init__(self, layesNeuronNum, activationFunc):
        self.activationFunc = activationFunc
        self.neurons = []
        self.loadData()
        self.createNodes(layesNeuronNum)

    def createNodes(self,layesNeuronNum):
        self.__addLayer(layesNeuronNum[0], 1)  #input layer
        for i in range(len(layesNeuronNum[1:])):
            self.__addLayer(layesNeuronNum[i], layesNeuronNum[i-1])

    def loadData(self):
        (self.xTrain, self.yTrain), (self.xTest, self.yTest) = mnist.load_data()

    def __addLayer(self, neuronsNum, inputsNum):
        self.neurons.append([Neuron(inputsNum) for i in range(neuronsNum)])

    def __setTrainExample(self, sampleIndex):
        for i in range(len(self.neurons[0])):
            self.neurons[0][i].setInput(self.xTrain[sampleIndex][i])

    def getLayerResult(self, layer):
        outputs = []
        for neuron in layer:
            outputs.append(neuron.output)
        return outputs

    def __mapConnections(self, sampleIndex):
        self.setTrainSet(sampleIndex)

        for index in range(len(self.neurons) - 1):
            result = self.getLayerResult(self.neurons[i])
            for i in range(len(self.neurons[index+1])):
                self.neurons[index+1][i].inputs = result

        self._sampleResult = self.getLayerResult(self.neurons[-1])

    def forwardPropagation(self, sampleIndex):
        self.__mapConnections(sampleIndex)
        for layerIndex in range(len(self.neurons)):
            for neuronIndex in range(len(self.neurons[layerIndex])):
                self.neurons[layerIndex][neuronIndex].computeValue()

    def backPropagation(self, sampleIndex):
        dW = 2*(self.h_x - self.output[sampleIndex])  #TODO: clac h(x)
        for layerIndex in range(len(self.neurons)-1, 0, -1): #layer index
            self.calcWeightsDelta(layerIndex, dW)

    def calcWeightsDelta(self, layerIndex, dW):
        for k in range(len(self.neurons[layerIndex])):
            for j in range(len(self.neurons[layerIndex-1])):
                dW *= self.neurons[layerIndex][k].partialDerivative()
                dW *= self.neurons[layerIndex-1][j].output()
                if layerIndex != len(self.neurons) - 1:
                    dW = affectOtherLayersDelta(layerIndex, dW, k)
                self.neurons[layerIndex][k].setDerivative(j, dW)

    def affectOtherLayersDelta(self, layerIndex, dW, k):
        derivativeSum = 0
        for l in range(len(self.neurons[layerIndex+1])):
            derivativeSum += self.neurons[layerIndex+1][l].getdW(k)*getW(k)
        dW *= derivativeSum
        return dW

def f(x):
    return 1 /(1 + math.e**(-x))

if __name__ == "__main__":
    x = Symbol('x')
    NN = NeuralNet([28, 5, 6, 10], f(x))
