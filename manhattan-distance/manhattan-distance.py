import numpy as np

def manhattan_distance(x, y):
    x, y = np.array(x), np.array(y)
    res = np.sum(np.abs(x - y))
    return float(res)