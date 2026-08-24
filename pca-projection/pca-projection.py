import numpy as np

def pca_projection(X: list, k: int) -> list:
    x_arr = np.array(X)

    x_center = x_arr - np.mean(x_arr, axis=0)
    cov_matrix = np.cov(x_center, rowvar=False)
    if cov_matrix.ndim == 0:
        cov_matrix = np.array([[cov_matrix]])

    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    sorted_indices = np.argsort(eigenvalues)[::-1]
    top_eigenvectors = eigenvectors[:, sorted_indices[:k]]
    projected_data = np.dot(x_center, top_eigenvectors)
    return projected_data.tolist()