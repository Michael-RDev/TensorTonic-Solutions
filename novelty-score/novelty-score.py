import math

def novelty_score(recommendations, item_counts, n_users):
    if not recommendations:
        return 0.0

    total_novelty = 0.0

    for item_idx in recommendations:
        popularity = item_counts[item_idx] / n_users
        item_novelty = -math.log2(popularity)
        total_novelty += item_novelty

    return total_novelty / len(recommendations)