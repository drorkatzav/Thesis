"""
"""
import itertools
import random
import pickle
import nnbp
import Configuration
import os
import StocksUtils
NETWORK_SIZES = [253, 10, 1]

class MyNet(object):
    DEFAULT_PATH = "/home/dror/Projects/thesis/test_runs"

    def __init__(self, trainging_set, testing_set, filename, network_sizes = NETWORK_SIZES, threshold = 0.5):
        self._training_set = trainging_set
        self._testing_set = testing_set
        self._threshold = threshold
        self._filename = os.path.join(self.DEFAULT_PATH, filename)
        self._network_sizes = network_sizes

    def create_patterns(self, training_set):
        """Create output patters for the training set"""
        patterns = []
        for line in training_set:
            symbol = StocksUtils.find_symbol_by_number(line[0])
            is_up = int(StocksUtils.is_stock_up(symbol))
            patterns.append((line[1], is_up))
        return patterns

    def save_results(self, result):
        f = file(self._filename, "wb")
        obj = (self._training_set,
               self._threshold,
               self._network,
               self._network_sizes,
               self._cycles, result)
        pickle.dump(obj, f)
        f.close()

    def full_run(self, cycles = 1):
        self._cycles = cycles
        #import pdb; pdb.set_trace()
        self._network_sizes[0] = len(self._training_set[0][1])
        self._network = nnbp.Network(self._network_sizes, threshold = self._threshold)
        patterns = self.create_patterns(self._training_set)
        self._network.train_patterns(patterns, self._cycles)
        test_result = self.test(self._network)
        #self.save_results(network, self._network_sizes, cycles, test_result)
        return test_result

    def compute_result(self, symbol_number):
        return StocksUtils.how_much_stock_up(StocksUtils.find_symbol_by_number(symbol_number))

    def test(self, network):
        test_result = 0
        for input_data in self._testing_set:
            network.set_input(input_data[1])
            network.run()
            net_result = float(network.get_output()[0])
            real_result = self.compute_result(input_data[0])
            test_result += net_result * real_result
        return test_result

def prepare_csv_to_analyze(filename):
    f = file(filename, "rb")
    lines = f.readlines()
    f.close()
    data = []
    for line in lines[1:]:
        fields = [s.strip() for s in line.split(',')]
        new_fields = []
        for field in fields[1:]:
            try:
                new_field = float(field)
            except:
                try:
                    #Maybe it is a date.
                    from datetime import date
                    date_string = field.split('/')
                    date_string.reverse()
                    date_int = [int(s) for s in date_string]
                    new_field = date(*date_int).toordinal()
                except:
                    #probably a string.
                    new_field = 0
            new_fields.append(new_field)
        try:
            symbol = StocksUtils.find_symbol_by_number(fields[0][2:])
            if None != StocksUtils.is_stock_up(symbol):
                data.append((fields[0][2:], new_fields))
        except:
            pass
    return data

def remain(full_list, selected):
    full_list_tmp = full_list[:]
    for part in selected:
        full_list_tmp.remove(part)
    return full_list_tmp

class Runners():

    def run_test(self, training_size):
        print "In run test"
        try:
            iterator = itertools.combinations(range(len(self._data)), training_size)
            best_net = None
            best_result = None
            for index, combination_index in enumerate(iterator):
                combination = [self._data[i] for i in combination_index]
                remainder = remain(self._data, combination)
                output_filename = "output_%s_%s" % (training_size, index)
                test_new = MyNet(list(combination), remainder, output_filename)
                print "Running test %s" % (index, )
                result = test_new.full_run()
                if None == best_result:
                    best_result = result
                    best_net = test_new
                if best_result < result:
                    best_result = result
                    best_net = test_new
            best_net.save_results(best_result)
        except Exception, e:
            best_net.save_results(best_result)
            raise e

    def prepare(self, filename, output_pkl = None):
        if not output_pkl:
            output_pkl = Configuration.OUTPUT_PICKLE
        self._data = prepare_csv_to_analyze(filename)
        f = file(output_pkl, "wb")
        pickle.dump(self._data, f)
        f.close()

    def run_10_test(self, training_size):
        print "Test for %s" %(training_size,)
        best_net = None
        best_result = None
        for j in range(10):
            comb_indexes = set()
            while len(comb_indexes) != training_size:
                comb_indexes.add(random.randrange(0,len(self._data)))
            combination = [self._data[x] for x in comb_indexes]
            remainder = remain(self._data, combination)
            output_filename = "output_%s" % (training_size,)
            test_new = MyNet(list(combination), remainder, output_filename)
            result = test_new.full_run()
            if None == best_result:
                best_result = result
                best_net = test_new
            if best_result < result:
                best_result = result
                best_net = test_new
        best_net.save_results(best_result)

    def test_all(self, filename = None):
        try:
            self._data = pickle.load(file(Configuration.OUTPUT_PICKLE, "rb"))
        except:
            self._data = self.prepare(filename)
        print "Data is Done!"
        for x in xrange(1, len(self._data)):
            self.run_10_test(x)

    def run_this(self):
        try:
            self._data = pickle.load(file(Configuration.OUTPUT_PICKLE, "rb"))
        except:
            self._data = self.prepare(filename)
        print "Data is Done!"
        self.test_all(1360)

    def try_all_second_layer(self):
        try:
            self._data = pickle.load(file(Configuration.OUTPUT_PICKLE, "rb"))
        except:
            self._data = self.prepare(filename)
        print "Starting"
        for i in range(271,506):
            network_sizes = [253, i, 1]
            print "Test for %s" %(i,)
            best_net = None
            best_result = None
            output_filename = "output_1360_%s" % (i,)
            for j in range(10):
                comb_indexes = set()
                while len(comb_indexes) != 1360:
                    comb_indexes.add(random.randrange(0,len(self._data)))
                combination = [self._data[x] for x in comb_indexes]
                remainder = remain(self._data, combination)
                test_new = MyNet(list(combination), remainder, output_filename, network_sizes = network_sizes)
                result = test_new.full_run()
                if None == best_result:
                    best_result = result
                    best_net = test_new
                if best_result < result:
                    best_result = result
                    best_net = test_new
            best_net.save_results(best_result)

#Run this with 1365.
#run_test('/home/dror/Projects/thesis/WRDS/scripts/output.csv', 10)
if __name__ == "__main__":
    Runners().try_all_second_layer()
