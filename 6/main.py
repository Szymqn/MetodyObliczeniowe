import math


def newton_progressive(xi, fi, x):
    result = fi[0]
    idx = len(xi)

    F = [[0 for _ in range(idx-1)]
         for _ in range(idx-1)]

    temp_x = []
    for i in range(len(F)):
        for j in range(len(F)):
            if i + j < len(F):
                if i == 0:
                    F[i][j] = fi[j+1] - fi[j]
                    temp_x.append(F[i][j])
                else:
                    if j < len(F[i-1]) - 1:
                        F[i][j] = F[i-1][j+1] - F[i-1][j]
                        temp_x.append(F[i][j])

    for j in range(len(F)):
        temp = ((F[j][0]) / (math.factorial(j+1) * math.pow(math.fabs(xi[1] - xi[0]), j+1)))
        for i in range(1, j+2):
            temp *= (x - xi[i-1])
        result += temp

    return result


if __name__ == '__main__':
    xi = [-4, -2, 0, 2, 4]
    fi = [-1011, -73, 1, -21, -523]
    x = 1

    print(f"Wynik dla x = {x}:", newton_progressive(xi, fi, x))
