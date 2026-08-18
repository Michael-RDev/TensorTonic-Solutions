import numpy as np

def matrix_trace(A):
    n = len(A)
    sum = 0
    for i in range(n):
        sum += A[i][i]
    return sum
