import numpy as np

def angle_between_3d(v, w):
    v, w = np.array(v), np.array(w)
    dot = np.dot(v, w)
    v_norm = np.linalg.norm(v)
    w_norm = np.linalg.norm(w)

    theta = np.arccos(dot / (v_norm * w_norm))
    return theta