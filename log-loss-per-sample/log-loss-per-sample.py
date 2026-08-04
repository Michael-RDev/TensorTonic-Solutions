import math

def log_loss(y_true, y_pred, eps=1e-15):
    losses = []
    for y, p in zip(y_true, y_pred):
        p_clipped = max(eps, min(p, 1 - eps))
        loss = -(y * math.log(p_clipped) + (1- y) * math.log(1 - p_clipped))
        losses.append(loss)
    return losses