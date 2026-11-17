import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    n, m = len(A), len(A[0])

    output = []
    for c in range(m):
        row = []
        for r in range(n):
            row.append(A[r][c])
        output.append(row)

    return np.array(output)