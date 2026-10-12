import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    n, c  = X.shape # num samples, num features

    w = np.zeros(c) # [0]
    b = 0.0

    for _ in range(steps):
        z = np.dot(X, w) + b 
        y_hat = _sigmoid(z)

        dz = y_hat - y
        dw = (1 / n) * np.dot(X.T, dz)
        db = (1 / n) * np.sum(dz)

        w -= lr * dw
        b -= lr * db
        

    return w, b