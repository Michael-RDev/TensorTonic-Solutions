import numpy as np

def matrix_trace(A):
    return sum(A[i][i] for i in range(len(A)))
