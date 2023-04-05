import numpy as np
from funcs import gauss


def newton_interpolation(xi, fi, x):
    n = len(xi)

    # empty 2d matrix
    F = [[0 for _ in range(n+2)]
         for _ in range(n+2)]

    for i in range(len(F)):
        for j in range(len(F)):
            if i < n and j < n:
                F[i][j] = xi[i] ** j

    print(np.asmatrix(F))


if __name__ == '__main__':

    xi = [1, 3, 5, 7]
    fi = [1, 8, 9, 17]
    x = 1

    print("Wartość interpolowana dla x =", x, "wynosi:", newton_interpolation(xi, fi, x))
