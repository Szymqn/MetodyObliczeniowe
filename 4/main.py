def newton_interpolation_diff(xi, fi, x):
    idx = len(xi)

    F = [[0 for _ in range(idx)]
         for _ in range(idx)]

    for i in range(idx):
        F[i][0] = fi[i]

    for i in range(1, idx):
        for j in range(idx - i):
            F[j][i] = (F[j + 1][i - 1] - F[j][i - 1]) / (xi[j + i] - xi[j])

    result = F[0][0]
    for i in range(1, idx):
        temp = F[0][i]
        for j in range(i):
            temp *= x - xi[j]
        result += temp
    return result


if __name__ == '__main__':
    xi = [-4, -2, 0, 2, 4]
    fi = [-1011, -73, 1, -21, -523]
    x = 1

    print(f"Wynik dla x = {x}:", newton_interpolation_diff(xi, fi, x))
