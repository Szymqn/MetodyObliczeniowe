import math
import numpy as np


def gauss_quadrature(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w


def gauss_legendre(f, lower_limit, upper_limit, n):
    result = 0
    quadrature = gauss_quadrature(n)
    abscissa = quadrature[0]
    weight = quadrature[1]

    h = (upper_limit - lower_limit) / 2

    for i in range(n):
        result += weight[i] * f(h * abscissa[i] + (upper_limit + lower_limit) / 2)

    return h * result


def legendre_poly(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre_poly(n - 1, x) - (n - 1) * legendre_poly(n - 2, x)) / n
