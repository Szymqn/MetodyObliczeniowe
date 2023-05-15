from funcs import gauss_legendre, gauss
from math import sqrt
import numpy as np


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
    print(results)

    for i in range(len(results)):
        result += results[i] * x ** i

    return result


if __name__ == '__main__':
    lower_limit = 1
    upper_limit = 3
    n = 2
    p_x = 1
    x = 2

    print(f"Wynik dla n = {n}, aproksymacja średniokwadratowa:", sqaure_approximation(lower_limit, upper_limit, n, p_x, x))

