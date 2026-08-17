def target_encoding(categories, targets):
    sums, counts = {}, {}
    for cat, target in zip(categories, targets):
        sums[cat] = sums.get(cat, 0.0) + target
        counts[cat] = counts.get(cat, 0) + 1

    means = {cat : sums[cat] / counts[cat] for cat in sums}
    return [means[cat] for cat in categories]