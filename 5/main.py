from math import pow
from funcs import gauss


def newton_interpolation(xi, fi):
    n = len(xi)

    # empty 2d matrix
    F = [[0 for _ in range(n+2)]
         for _ in range(n+2)]

    # modify fi
    fi.extend([1, 1])
    print(fi)

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

    return gauss(F, fi)


if __name__ == '__main__':

    xi = [1, 3, 5, 7]
    fi = [1, 8, 9, 17]

    print("Wartość interpolowana wynosi:", newton_interpolation(xi, fi))
