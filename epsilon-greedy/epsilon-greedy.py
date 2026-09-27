import numpy as np

def epsilon_greedy(q_values: list, epsilon: float, seed: int = 0) -> int:
    rng = np.random.default_rng(seed)

    u = rng.random()

    if u < epsilon:
        action = rng.integers(0, len(q_values))
    else:
        action = np.argmax(q_values)
    return int(action)