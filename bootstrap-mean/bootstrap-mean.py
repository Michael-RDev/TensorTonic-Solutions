import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    x = np.asarray(x, dtype=float)

    n = len(x)
    if rng is not None:
        indices = rng.integers(0, n, size=(n_bootstrap, n))
    else:
        indices = np.random.randint(0, n, size=(n_bootstrap, n))
    
    samples = x[indices]
    boot_mean = samples.mean(axis=1) #(1000, )
    
    alpha = 1 - ci
    lower = np.quantile(boot_mean, alpha/2)
    upper = np.quantile(boot_mean, 1-alpha/2)
    return boot_mean, lower, upper
    
    
