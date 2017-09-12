import numpy as np
import Neuron from .Neuron

class NeuralNet:
    def __init__(self, layesNeuronNum, activationFunc):
        self.activationFunc = activationFunc
        self.neurons = []
        self.inputs = []
        self.outputs = []
        self.createNodes(layesNeuronNum)

    def createNodes(self,layesNeuronNum):
        self.__addLayer(layesNeuronNum[0], 1)  #input layer
        for i in range(len(layesNeuronNum[1:])):
            self.__addLayer(layesNeuronNum[i], layesNeuronNum[i-1])

    def __addLayer(self, neuronsNum, inputsNum):
        self.neurons.append([Neuron(inputsNum) for i in range(neuronsNum)])

    def setTrainSet(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def __setTrainExample(self, sampleIndex):
        for i in range(len(self.neurons[0])):
            self.neurons[0][i].setInput(self.inputs[sampleIndex][i])]

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
