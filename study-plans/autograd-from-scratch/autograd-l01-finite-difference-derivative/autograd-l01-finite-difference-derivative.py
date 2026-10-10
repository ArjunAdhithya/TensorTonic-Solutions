import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    f_x = 0.0
    f_xh = 0.0

    for k in range(len(coefficients)):
        f_x += coefficients[k] * (x ** k)
        f_xh += coefficients[k] * ((x + h) ** k)

    slope = (f_xh - f_x) / h

    return float(f_x), float(f_xh), float(slope)
    # pass
