import numpy as np
from math import sqrt


def gauss_quadrature(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w


def gauss_legendre(lower_limit, upper_limit, n, p_x, j, k):
    result = 0
    quadrature = gauss_quadrature(n)
    abscissa = quadrature[:][0]
    weight = quadrature[:][1]

    h = (upper_limit - lower_limit) / 2

    integral_r = lambda x, p_x, idx: x ** idx * sqrt(x ** 3 + 3 * x ** 2 + 1) * p_x
    integral_m = lambda x, p_x, idx_x, idx_y: x ** idx_x * x ** idx_y * p_x

    for i in range(n):
        if k is None:
            result += weight[i] * integral_r(h * abscissa[i] + (upper_limit + lower_limit) / 2, p_x, j)
        else:
            result += weight[i] * integral_m(h * abscissa[i] + (upper_limit + lower_limit) / 2, p_x, j, k)

    return h * result


def gauss(matrix, vector):
    n = len(matrix)

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if matrix[j][i] > matrix[max_row][i]:
                max_row = j

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            vector[j] -= factor * vector[i]

            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (vector[i] - sum(matrix[i][j] * x[j] for j in range(i + 1, n))) / matrix[i][i]

    return x
