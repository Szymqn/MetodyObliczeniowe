import numpy as np


def gauss_quadrature(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w


def integral(x):
    return (x - 1) / (x ** 2 + x)


def gauss_legendre(lower_limit, upper_limit, n):
    result = 0
    quadrature = gauss_quadrature(n)
    abscissa = quadrature[:][0]
    weight = quadrature[:][1]

    h = (upper_limit - lower_limit) / 2

    for i in range(n):
        print(i)
        result += weight[i] * integral(h * abscissa[i] + (upper_limit + lower_limit)/2)

    return h * result


if __name__ == '__main__':
    lower_limit = 2
    upper_limit = 3
    n = 2

    print(gauss_legendre(lower_limit, upper_limit, n))
