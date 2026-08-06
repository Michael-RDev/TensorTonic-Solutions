def precision_recall_at_k(recommended, relevant, k):
    if not relevant or k == 0:
        return 0.0, 0.0

    top_k_recommended = recommended[:k]
    relavant_set = set(relevant)
    hits = sum(1 for item in top_k_recommended if item in relavant_set)
    precision = hits / k
    recall = hits / len(relavant_set)

    return [precision, recall]