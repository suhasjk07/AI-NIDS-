import numpy as np

def generate_synthetic_flows(n):
    bytes_ = np.random.lognormal(mean=8, sigma=1, size=n)
    packets = np.random.poisson(lam=20, size=n)
    duration = np.random.exponential(scale=1.0, size=n)
    bpp = bytes_/np.maximum(packets,1)
    X = np.vstack([bytes_, packets, duration, bpp]).T
    return X
