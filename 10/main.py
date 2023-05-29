import math
import numpy as np
from scipy.integrate import quad


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


def approx_legendre(f, n, a, b, x):
    coefficients = []
    lambdas = []

    for i in range(n + 1):
        phi_i = lambda x: legendre_poly(i, x)
        phi_i_squared = lambda x: phi_i(x) ** 2

        quad_result = gauss_legendre(phi_i_squared, a, b, 20)
        lambdas.append(quad_result)

        C_i = gauss_legendre(lambda x: phi_i(x) * f(x), a, b, 20) / quad_result
        coefficients.append(C_i)

    return sum(coefficients[i] * legendre_poly(i, x) for i in range(n + 1))


if __name__ == '__main__':
    f = lambda x: math.exp(x)
    n = 2
    a = -1
    b = 1
    x = 1

    g_x = approx_legendre(f, n, a, b, x)
    print("interpolation: g({}) = {}".format(x, g_x))
    print("expected: f({}) = {}".format(x, f(x)))
