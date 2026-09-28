def cumulative_returns(returns: list) -> list:
    wealth = 1.0
    cum_returns = []

    for r in returns:
        wealth = wealth * (1 + r)
        cum_returns.append(wealth - 1)

    return cum_returns