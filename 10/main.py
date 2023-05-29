import numpy as np
import math
from funcs import gauss_quadrature, gauss_legendre, legendre_poly


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
