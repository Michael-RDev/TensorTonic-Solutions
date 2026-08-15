import math

def log_transform(values):
    return [math.log1p(values[i]) for i in range(len(values))]