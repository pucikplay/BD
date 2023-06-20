import random
import matplotlib.pyplot as plt
import scipy.stats

class Bucket: # basically Vitter
    def __init__(self):
        self.idx = None
        self.val = None
        self.viewed = 0

    def onGet(self, z):
        self.viewed += 1
        if random.random() <= (1 / self.viewed):
            self.idx = self.viewed
            self.val = z

    def readData(self):
        return self.idx, self.val
    

class Window:
    def __init__(self, window_size):
        self.partial = Bucket()
        self.active = None
        self.window_size = window_size

    def onGet(self, z):
        self.partial.onGet(z)
        if self.partial.viewed == self.window_size: # Partial becomes active, new partial is created
            self.active = self.partial
            self.partial = Bucket()

    def readData(self):
        if self.active is None: # case for first n elements
            (_, partial_val) = self.partial.readData()
            return partial_val
        else:
            (active_idx, active_val) = self.active.readData()
            (_, partial_val) = self.partial.readData()

            if active_idx <= self.partial.viewed:
                return partial_val
            else:
                return active_val
            
    def readIdx(self):
        if self.active is None: # case for first n elements
            (partial_idx, _) = self.partial.readData()
            return partial_idx - 1
        else:
            (active_idx, _) = self.active.readData()
            (partial_idx, _) = self.partial.readData()

            if active_idx <= self.partial.viewed:
                return (partial_idx - 1) + (self.window_size - self.partial.viewed)
            else:
                return (active_idx - 1) - self.partial.viewed
            
def histogram_gen():
    window_size = 5
    no_tests = 100
    stream_len = 1000

    sample = []
    for _ in range(no_tests):
        window = Window(window_size)
        for i in range(stream_len):
            window.onGet(i)
            sample.append(window.readData())

    plt.hist(sample, density=True, bins=stream_len)
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Distribution: window_size = 5, stream_len = 1000')
    plt.savefig('z25.png', dpi=300)

def chi_sq_test():
    window_size = 5
    stream_len = 10000
    frequencies = [0] * window_size

    window = Window(window_size)
    for i in range(stream_len):
        window.onGet(i)
        frequencies[window.readIdx()] += 1

    (chi_sq, p) = scipy.stats.chisquare(frequencies)
    print("Chi_square stat: {}, p_value: {}".format(chi_sq, p))

if __name__ == "__main__":
    histogram_gen()
    chi_sq_test()