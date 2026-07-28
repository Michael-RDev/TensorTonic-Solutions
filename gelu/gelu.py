import numpy as np
import math

def gelu(x):
    x = np.array(x)
    erf_vec = np.vectorize(math.erf)
    inside_term = 1 + erf_vec(x / np.sqrt(2))
    outside_term = 0.5 * x
    return outside_term * inside_term