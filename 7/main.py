import numpy as np
from math import sqrt


def integral(x):
    # return x ** 2
    return (sqrt(x ** 2 + .3))/(1.4 + sqrt(.8 * (x ** 2) + 1.6))


def trapeze_method(integral, lower_limit, upper_limit, n):
    result = 0
    results = []
    h = round((upper_limit - lower_limit) / n, 1)

    for i in np.arange(lower_limit, upper_limit+h, h):
        results.append(integral(i))

    for i in range(len(results)):
        if i == 0 or i == len(results)-1:
            result += results[i] / 2
        else:
            result += results[i]

    return h * result


def simpson_method(integral, lower_limit, upper_limit, n):
    results = []
    h = (upper_limit - (upper_limit - lower_limit)) / 2

    for i in np.arange(lower_limit, upper_limit+h, h):
        results.append(integral(i))

    result = results[0] + results[-1]

    for i in range(1, len(results)-1):
        if i % 2 == 0:
            result += 2 * results[i]
        else:
            result += 4 * results[i]

    return result * h / 3


if __name__ == '__main__':
    # lower_limit = 1
    # upper_limit = 4
    # n = 3

    lower_limit = 1.3
    upper_limit = 2.5
    print("Podaj n: ", end='')
    n = int(input())

    print(f"Wynik dla n = {n}, moteda trapezów:", trapeze_method(integral, lower_limit, upper_limit, n))
    print(f"Wynik dla n = {n}, metoda simpsona:", simpson_method(integral, lower_limit, upper_limit, n))
