from math import sqrt
from funcs import gauss


def smallest_square(x, y, n, m, point):
    result = 0

    F = [[0 for _ in range(m + 1)]
         for _ in range(m + 1)]

    F_res = [0 for _ in range(m + 1)]

    for j in range(len(F)):
        for k in range(len(F)):
            for i in range(n):
                F[j][k] += (x[i] ** (k + j))

    for k in range(len(F_res)):
        for i in range(n):
            F_res[k] += (x[i] ** k) * y[i]

    results = gauss(F, F_res)

    for i in range(len(results)):
        result += results[i] * (point ** i)

    return result


if __name__ == '__main__':
    square_root = lambda x: sqrt(x ** 3 + 3 * x ** 2 + 1)
    x = [-1, -.5, 0, .5, 1]
    y = [square_root(i) for i in x]

    # square_root = lambda x: sqrt(x)
    # x = [1, 2, 3, 4]
    # y = [6, 19, 40, 69]

    n = 5
    m = 4
    point = .25

    smallest_square(x, y, n, m, point)
    print(f"Wynik dla n = {n} i m = {m}, w punkcie x = {point}, aproksymacja najmniejszych kwadratów wynosi:", smallest_square(x, y, n, m, point))
    print(f"Wynik oczekiwany dla n = {n} i m = {m}, w punkcie x = {point}, wynosi:", square_root(point))
