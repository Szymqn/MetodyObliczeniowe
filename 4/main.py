def newton_interpolation(xi, fi, x):
    n = len(xi)

    # empty 2d matrix
    F = [[0 for _ in range(n)]
         for _ in range(n)]

    for i in range(n):
        F[i][0] = fi[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (xi[i + j] - xi[i])

    result = F[0][0]
    for j in range(1, n):
        term = F[0][j]
        for i in range(j):
            term *= (x - xi[i])
        result += term
    return result


if __name__ == '__main__':
    # Sprawozdanie result: -1
    # xi = [-4, -2, 0, 2, 4]
    # fi = [-1011, -73, 1, -21, -523]
    # x = 1

    xi = [0, 2, 3, 4, 6]
    fi = [1, 3, 2, 5, 7]
    x = 1

    wynik = newton_interpolation(xi, fi, x)

    print("Wartość interpolowana dla x =", x, "wynosi:", wynik)
