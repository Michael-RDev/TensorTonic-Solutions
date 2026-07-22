import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    x = np.array(x)
    return lam * np.where(x > 0, x, alpha * (np.exp(x) - 1))