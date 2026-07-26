import numpy as np

def clip_gradients(g, max_norm):
 
    g = np.array(g)

    if max_norm <= 0:
        return g
    g_mag = np.sqrt(np.sum(np.square(g)))

    if g_mag > max_norm:
        g = g * (max_norm / g_mag)
    
    return g