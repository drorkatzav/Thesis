import Configuration
import pickle
import numpy
import random

class Network(object):
    def __init__(self, layers_sizes, learning_rate = 0.1, threshold = 0):
        self._learning_rate = learning_rate
        self._layers = [numpy.zeros(layer_size) for layer_size in layers_sizes]
        self._weights = []
        for layer_index in xrange(len(layers_sizes) - 1):
            l = []
            for j in xrange(layers_sizes[layer_index + 1]):
                s = []
                for i in xrange(layers_sizes[layer_index]):
                    s.append(random.random())
                l.append(s)
            self._weights.append(numpy.array(l))
        # self._weights = [numpy.array([random.random()
        #                                 for i in xrange(layres_sizes[layer_index])]
        #                                for j in xrange(layers_sizes[layer_index + 1]))
        #                  for layer_index in xrange(len(layers_sizes) - 1)]
        self._threshold = threshold

    def set_input(self, input_layer):
        self._layers[0] = numpy.asarray(input_layer)

    def get_output(self):
        return self._layers[-1].tolist()

    def load_weights(self, filename = Configuration.WEIGHTS_FILE):
        self._weights = pickle.load(file(filename, "rb"))

    def save_weights(self, filename = Configuration.WEIGHTS_FILE):
        pickle.dump(self._weights, file(filename, "wb"))

    def train(self, input_pattern, output_pattern, cycles = 1):
        output_array = numpy.asarray(output_pattern)
        self.set_input(input_pattern)
        for i in xrange(cycles):
            self.run()
            self.backprop(output_array)

    def train_patterns(self, patterns, cycles = 1):
        for i in xrange(cycles):
            for input_pattern, output_pattern in patterns:
                self.train(input_pattern, output_pattern)

    def run(self):
        for layer_index in xrange(len(self._layers) - 1):
            next_layer_tmp = numpy.dot(self._weights[layer_index],
                                       self._layers[layer_index])
            next_layer = next_layer_tmp / len(self._layers[layer_index])
            self._layers[layer_index + 1] = self.threshold(self.transfer(next_layer))

    def backprop(self, desired_output):
        deltas = self.transfer_derivative(self._layers[-1] *
                                          (desired_output - self._layers[-1]))
        self.generalized_delta_rule(deltas, len(self._layers) - 2)
        for layer_counter in xrange(len(self._layers) - 2, 0, -1):
            deltas = self.transfer_derivative(self._layers[layer_counter]) * numpy.dot(deltas,
                                                                                       self._weights[layer_counter])
            self.generalized_delta_rule(deltas, layer_counter - 1)

    def generalized_delta_rule(self, deltas, layer_number):
        self._weights[layer_number] += self._learning_rate * numpy.outer(deltas,
                                                                         self._layers[layer_number])
    def transfer(self, x):
            return 1 / (1 + numpy.e ** (-1 * x))

    def transfer_derivative(self, x):
        return (1 - x) * x

    def threshold(self, x):
        return ((x - self._threshold) / (1-self._threshold))
