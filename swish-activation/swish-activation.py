import numpy as np

def swish(x):
    x = np.array(x, dtype=float)

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    return x * sigmoid(x)