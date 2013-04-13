"""
"""
import nnbp
import Configuration
import Numeric

def stock(buffer):
    network = nnbp.Network(Configuration.NETWORK_SIZES)
    network.load_weights(Configuration.WEIGHTS_FILE)
    input_data = buffer.read()
    netwrok.set_input(input_data)
    network.run()
    output = network.get_output()
    return "What to do with this output? %s" % (output, )

if __name__ == "__main__":
    import sys
    file_data = file(sys.argv[1], "rb").read()
    stock(file_data)
