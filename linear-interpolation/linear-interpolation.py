def linear_interpolation(values):
    n = len(values)
    results = [0.0] * n

    for i in range(n):
        if values[i] is not None:
            results[i] = float(values[i])
        else:
            prev = i - 1
            while prev >= 0 and values[prev] is None:
                prev -= 1

            next = i + 1
            while next < n and values[next] is None:
                next += 1

            if prev >= 0 and next < n:
                y0, y1 = values[prev], values[next]
                results[i] = y0 + (y1 - y0) * (i - prev) / (next - prev)
            elif prev >= 0:
                results[i] = float(values[prev])
            elif nxt < n:
                results[i] = float(values[next])

    return results
    