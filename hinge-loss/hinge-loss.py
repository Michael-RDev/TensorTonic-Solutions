import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    y_true, y_score = np.asarray(y_true), np.asarray(y_score)
    loss = np.maximum(0, margin - y_true * y_score)
    if reduction == "mean":
        return np.mean(loss)
    elif reduction == "sum":
        return np.sum(loss)
    elif reduction is None:
        return loss
    else:
        raise ValueError(f"Invalid reduction: {reduction}. Expected 'mean', 'sum', or None.")