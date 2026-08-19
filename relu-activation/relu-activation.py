import numpy as np

def relu(x):
    x_array = np.array(x)
    return np.maximum(0,x_array)