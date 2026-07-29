import numpy as np

def apply_homogeneous_transform(T, points):
    T, points = np.array(T), np.array(points)
    original_ndim = points.ndim
    points = np.atleast_2d(points)  #(D,) -> (1, D) else (N, D)
    N, D = points.shape

    ones = np.ones((N, 1), dtype=points.dtype) #(N, 1)
    points_h = np.hstack([points, ones]) #(N, D+1)
    transformed = points_h @ T.T
    w = transformed[:, -1:]
    w = np.where(w == 0, 1e-8, w)
    transformed_points = transformed[:, :-1] /  w
    if original_ndim == 1:
        return transformed_points.flatten()
    return transformed_points
    
    
    
    
        