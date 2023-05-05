from math import sqrt


def integral(x):
    # return (sqrt(x ** 2 + .3))/(1.4 + sqrt(.8 * (x ** 2) + 1.6))
    return x ** 2


def trapeze_method(integral, lower_limit, upper_limit, n):
    result = 0
    results = []
    lower_limit *= 10
    upper_limit *= 10
    h = round((upper_limit - lower_limit) / n, 1)

    for i in range(int(lower_limit), int(upper_limit)+int(h), int(h)):
        results.append(integral(i/10))

    for i in range(len(results)):
        if i == 0 or i == len(results)-1:
            result += results[i] / 2
        else:
            result += results[i]

    return h * result / 10


if __name__ == '__main__':
    lower_limit = 1
    upper_limit = 4
    n = 3

    # lower_limit = 1.3
    # upper_limit = 2.5
    # n = 3

    print(f"Wynik dla n = {n}:", trapeze_method(integral, lower_limit, upper_limit, n))
