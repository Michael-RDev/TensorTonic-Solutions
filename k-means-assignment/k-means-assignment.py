def k_means_assignment(points: list, centroids: list) -> list:
    assignments =[]
    for point in points:
        min_dist = float('inf')
        best_centroid = -1

        for i, centroid in enumerate(centroids):
            dist = sum((p - c) ** 2 for p, c in zip(point, centroid))

            if dist < min_dist:
                min_dist = dist
                best_centroid = i
        assignments.append(best_centroid)
    return assignments