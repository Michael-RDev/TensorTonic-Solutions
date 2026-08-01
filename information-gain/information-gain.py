import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    y = np.array(y)
    N = len(y)
    split_mask = np.array(split_mask, dtype=bool)

    y_left = y[split_mask]
    y_right = y[~split_mask]

    n_left = len(y_left)
    n_right = len(y_right)
    if n_left == 0 or n_right == 0:
        return 0.0

    return _entropy(y) - ((n_left / N) * _entropy(y_left) +  (n_right / N) * _entropy(y_right))

    
