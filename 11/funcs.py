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

    print(F)
    print(F_res)

    results = gauss(F, F_res)

    for i in range(len(results)):
        result += results[i] * (point ** i)

    print(result)


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
