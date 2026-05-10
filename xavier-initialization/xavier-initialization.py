def xavier_initialization(W, fan_in, fan_out):
    limit = (6 / (fan_in + fan_out)) ** 0.5
    new_weights = [[(weight * 2 * limit) - limit for weight in row] for row in W]
    return new_weights