import numpy as np

def vector_norm_3d(v):
    v = np.array(v)
    if v.shape == (3, ):
        return float(np.linalg.norm(v))

    if v.ndim == 2 and v.shape[1] == 3:
        return np.linalg.norm(v, axis=1)