def autocorrelation(series: list, max_lag: int) -> list:
    n = len(series)


    mean_x = sum(series) / n
    centered = [x - mean_x for x in series]
    gamma_0 = sum(x ** 2 for x in centered)
    
    result = []
    for k in range(max_lag + 1):
        if gamma_0 == 0:
            result.append(1.0 if k == 0 else 0.0)
            continue
        numerator = sum(centered[t] * centered[t + k] for t in range(n - k))
        rk = numerator / gamma_0
        result.append(round(rk, 6))
        
    return result