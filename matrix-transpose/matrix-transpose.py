import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    m, n = len(A), len(A[0])

    res = [[0] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            res[r][c] = A[c][r]

    return np.array(res)
        