def lag_features(series: list, lags: list) -> list:
    max_lag = max(lags)
    return [
        [series[i - lag] if i - lag >= 0 else None for lag in lags] 
        for i in range(max_lag, len(series))
    ]