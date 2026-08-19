import numpy as np

def leaky_relu(x, alpha=0.01):
    x_array = np.asarray(x)
    return np.maximum(alpha * x_array, x_array)