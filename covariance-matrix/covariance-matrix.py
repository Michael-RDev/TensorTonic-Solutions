import numpy as np

def covariance_matrix(X):
    x = np.array(X)
    N = x.shape[0]
    if x.ndim != 2 or N <  2 or np.isnan(x).any():
        return None
    
    
    mu = np.mean(x, axis=0)
    x_centerd = x - mu
    
    cov_mat = (x_centerd.T @ x_centerd) / (N - 1) + 1e-10
    return cov_mat