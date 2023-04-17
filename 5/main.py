from math import pow
from funcs import gauss


def newton_interpolation(xi, fi, x, l_derivative, r_derivative):
    result = 0
    n = len(xi)

    # empty 2d matrix
    F = [[0 for _ in range(n+2)]
         for _ in range(n+2)]

    # modify fi
    fi.extend([l_derivative, r_derivative])

    first_node = xi[0]
    last_node = xi[-1]

    for i in range(len(F)):
        c = i - 1
        for j in range(len(F)):
            if i < n:
                if j < n:
                    F[i][j] = xi[i] ** j
                elif i > 1:
                    F[i][j] = pow(xi[i] - xi[i-c], 3)
                    c -= 1
            else:
                if 0 < j < n:
                    F[-2][j] = pow(j, first_node)
                    F[-1][j] = pow(last_node, j-1) * j
                elif j >= n:
                    F[-1][j] = 3 * pow((last_node - xi[j-3]), 2)

    results = gauss(F, fi)

    for i in range(len(results)):
        if i < len(xi):
            result += results[i] * pow(x, i)
        else:
            result += results[i] * pow((x - xi[i-n+1]), 3)

    return round(result, 2)


if __name__ == '__main__':
    xi = [-1011, -73, 1, -21, -523]
    fi = [-4, -2, 0, 2, 4]
    l_derivative = 957
    r_derivative = -579
    x = 1

    print("Wartość interpolowana wynosi:", newton_interpolation(xi, fi, x, l_derivative, r_derivative))
