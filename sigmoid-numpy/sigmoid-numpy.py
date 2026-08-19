import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x_array = np.array(x)
    deno = 1 + np.exp(-x_array)
    sig = 1/deno
    return sig