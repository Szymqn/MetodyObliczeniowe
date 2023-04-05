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
        x[i] = round((vector[i] - sum(matrix[i][j] * x[j] for j in range(i + 1, n))) / matrix[i][i])

    return x
