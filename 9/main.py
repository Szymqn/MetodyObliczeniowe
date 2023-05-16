from funcs import gauss_legendre, gauss
from math import sqrt
import numpy as np


def expected_result(x):
    return sqrt(x ** 3 + 3 * x ** 2 + 1)
    # return sqrt(x)


def sqaure_approximation(lower_limit, upper_limit, n, p_x, x):
    result = 0

    F = [[0 for _ in range(n+1)]
         for _ in range(n+1)]

    F_res = [0 for _ in range(n+1)]

    for i in range(len(F)):
        for j in range(len(F)):
            F[i][j] = gauss_legendre(lower_limit, upper_limit, 20, p_x, i, j)

    for i in range(len(F_res)):
        F_res[i] = gauss_legendre(lower_limit, upper_limit, 20, p_x, i, None)

    results = gauss(F, F_res)

    for i in range(len(results)):
        result += results[i] * x ** i

    return result


if __name__ == '__main__':
    n = 5
    p_x = 1

    lower_limit = -1
    upper_limit = 1
    x = .25

    print(f"Wynik dla n = {n}, w punckie x = {x}, aproksymacja średniokwadratowa wynosi:", sqaure_approximation(lower_limit, upper_limit, n, p_x, x))
    print(f"Wynik oczekiwany dla n = {n}, w punkcie x = {x}:", expected_result(x))
