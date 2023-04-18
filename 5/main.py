from math import pow
from funcs import gauss
import numpy as np


def newton_interpolation(xi, fi, x, l_derivative, r_derivative):
    result = 0
    n = len(xi)

    F = [[0 for _ in range(n+2)]
         for _ in range(n+2)]

    fi.extend([l_derivative, r_derivative])

    first_el = xi[0]
    last_el = xi[-1]

    for i in range(len(F)):
        for j in range(len(F)):
            if i < n:
                if j < n-1:
                    F[i][j] = xi[i] ** j
                if i > 1 and j >= n-1:
                    F[i][j] = pow(xi[i] - xi[j-3], 3)

    F[-1][1] = 1
    F[-1][2] = 2 * last_el
    F[-1][3] = 3 * pow(last_el, 2)

    for i in range(1, len(F)):
        if i < 4:
            F[i][-1] = 0
            F[-2][i] = i * pow(first_el, i-1)
        else:
            F[-1][i] = 3 * pow(last_el - xi[i-3], 2)

    np.set_printoptions(suppress=True)
    print(np.asmatrix(F))
    print(fi)
    results = gauss(F, fi)
    print(results)

    for i in range(len(results)):
        if i < len(xi):
            result += results[i] * pow(x, i)
        else:
            result += results[i] * pow((x - xi[i-n+1]), 3)

    return result


if __name__ == '__main__':
    xi = [-4, -2, 0, 2, 4]
    fi = [-1011, -73, 1, -21, -523]
    l_derivative = 957
    r_derivative = -579
    x = 1

    print(f"Wynik dla x = {x}:", newton_interpolation(xi, fi, x, l_derivative, r_derivative))
