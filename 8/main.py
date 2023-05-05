import numpy as np
from math import sqrt


def gauss_quadrature(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w


def integral(x):
    # return (x - 1) / (x ** 2 + x)
    return (sqrt(x ** 2 + .3))/(1.4 + sqrt(.8 * (x ** 2) + 1.6))


def gauss_legendre(lower_limit, upper_limit, n):
    result = 0
    quadrature = gauss_quadrature(n)
    abscissa = quadrature[:][0]
    weight = quadrature[:][1]

    h = (upper_limit - lower_limit) / 2

    for i in range(n):
        result += weight[i] * integral(h * abscissa[i] + (upper_limit + lower_limit)/2)

    return h * result


if __name__ == '__main__':
    # lower_limit = 2
    # upper_limit = 3
    # n = 2

    lower_limit = 1.3
    upper_limit = 2.5
    print("Podaj n: ", end='')
    n = int(input())

    print(f"Wynik dla n = {n}:", gauss_legendre(lower_limit, upper_limit, n))
