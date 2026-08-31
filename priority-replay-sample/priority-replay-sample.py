def priority_replay_sample(priorities: list, alpha: float, beta: float) -> list:
    n = len(priorities)
    powered_priorities = [p ** alpha for p in priorities]
    sum_powred = sum(powered_priorities)
    if sum_powred == 0:
        probs = [1.0 / n] * n
    else:
        probs = [p / sum_powred for p in powered_priorities]

    weights = []
    for p in probs:
        if p == 0 and beta > 0:
            weights.append(float('inf'))
        else:
            weights.append((n * p) ** (-beta))

    max_w = max(weights) if weights else 0.0
    if max_w == 0.0 or max_w == float('inf'):
        norm_weights = [1] * n
    else:
        norm_weights = [w / max_w for w in weights]
    return [probs, norm_weights]