import numpy as np


def newton_progressive(x, f, n):
    result = f[0]
    m = len(x)

    # empty 2d matrix
    F = [[0 for _ in range(m-1)]
         for _ in range(m-1)]

    print('x:', x)
    print('f(x):', f)

    temp_p = int(len(x) / 2)
    pos = temp_p * -1
    c = pos
    temp_x = []
    for i in range(len(F)):
        for j in range(len(F)):
            if i + j < len(F):
                if i == 0:
                    F[i][j] = f[j+1] - f[j]
                    temp_x.append(F[i][j])
                else:
                    F[i][j] = temp_x[i+j+c] - temp_x[i+j+c-1]
                    temp_x.append(F[i][j])
        c += temp_p

    for j in range(len(F)):
        temp = ((F[j][0])/(np.math.factorial(j+1) * np.math.pow(np.math.fabs(x[1]-x[0]), j)))
        for i in range(1, j+2):
            temp *= (n - i)
        result += temp

    return result


if __name__ == '__main__':
    # x = [-4, -2, 0, 2, 4]
    # f = [-1011, -73, 1, -21, -523]
    # n = 1

    x = [1, 2, 3, 4]
    f = [3, 7, 8, 15]
    n = 2.5

    print("Wartość interpolowana wynosi:", newton_progressive(x, f, n))
