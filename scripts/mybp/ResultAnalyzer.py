import os
import pickle

class NotYetImplemented(Exception):
    pass
class Handler(object):
    def __init__(self):
        return
    def handle(self, result):
        raise NotYetImplemented

class GetMaxHandler(Handler):
    def __init__(self):
        super(GetMaxHandler, self).__init__()
        self._max = None
        self._best = None
    def handle(self, result, filename):
        if None == self._max:
            self._max = result[-1]
            self._best = filename
        if result[-1] > self._max:
            self._max = result[-1]
            self._best = filename
    def show(self):
        return (self._max, self._best)

class GetGraph(Handler):
    def __init__(self):
        super(GetGraph, self).__init__()
	self._output = file('result.out', 'wb')
    def handle(self, result, filename):
        number = int(filename[filename.index('_')+1:])
        self._output.write("%s, %s\n" % (number, result[-1]))
	self._output.flush()
    def show(self):
	self._output.close()
        print 'Done'

def ResultAnalyzer(path, handler):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            f = file(os.path.join(dirpath, filename), "rb")
            result = pickle.load(f)
            f.close()
            handler.handle(result, filename)
    return handler.show()

if __name__ == "__main__":
    import sys
    if 2 != len(sys.argv):
        print "USAGE: python ResultAnalyzer.py <results path>"
        exit(1)
    print ResultAnalyzer(sys.argv[1], GetGraph())
