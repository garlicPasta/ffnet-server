from ffnet import ffnet, mlgraph

# Define training data
input = [[0., 0.], [0., 1.], [1., 0.], [1., 1.]]
target = [[1.], [0.], [0.], [1.]]
### XOR problem example for ffnet ###
class Nn:

# Generate standard layered network architecture and create network
    def __init__(self):
        conec = mlgraph((2, 2, 1))
        self.net = ffnet(conec)

# Train network
#first find good starting point with genetic algorithm (not necessary, but may be helpful)

    def set_weights(self):
        print "FINDING STARTING WEIGHTS WITH GENETIC ALGORITHM..."
        self.net.train_genetic(input, target, individuals=20, generations=500)
        #then train with scipy tnc optimizer

    def train_network(self):
        print "TRAINING NETWORK..."
        self.net.train_tnc(input, target, maxfun=1000, messages=1)

    # Test network
    def test_network(self):
        print "TESTING NETWORK..."
        output, regression = self.net.test(input, target, iprint=2)

    def save_network(self):
        # Save/load/export network
        from ffnet import savenet, loadnet, exportnet

        print "Network is saved..."
        savenet(self.net, "xor.net")
        print "Network is reloaded..."
        net = loadnet("xor.net")
        print "Network is tested again, but nothing is printed..."
        output, regression = net.test(input, target, iprint=0)
        print
        print "Exporting trained network to the fortran source..."
        exportnet(net, "xor.f")
        print "Done..."
        print "Look at the generated xor.f file."
        print "Note: you must compile xor.f along with the ffnet.f"
        print "file which can be found in ffnet sources."
