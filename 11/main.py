from math import sqrt
from funcs import smallest_square


def square_root(x):
    # return sqrt(x+2)
    return sqrt(x ** 3 + 3 * x ** 2 + 1)


if __name__ == '__main__':
    x = [-1, -.5, 0, .5, 1]
    y = [square_root(i) for i in x]

    # x = [1, 2, 3, 4] 
    # y = [6, 19, 40, 69]

    n = 5
    m = 4
    point = .25

    smallest_square(x, y, n, m, point)
    print(square_root(point))

