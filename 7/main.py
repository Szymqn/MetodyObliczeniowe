from math import sqrt


def integral(x):
    return (sqrt(x ** 2 + .3))/(1.4 + sqrt(.8 * (x ** 2) + 1.6))


def trapeze_method(integral, lower_limit, upper_limit, n):
    result = 0
    results = []
    h = (upper_limit - lower_limit) / n

    for i in range(1, upper_limit+1):
        results.append(integral(i))

    print(results)

    for i in range(upper_limit):
        if i == 0 or i == len(results)-1:
            result += results[i] / 2
        else:
            result += results[i]

    return h * result


if __name__ == '__main__':
    lower_limit = 1.3
    upper_limit = 2.5
    n = 3

    print(f"Wynik dla n = {n}:", trapeze_method(integral, lower_limit, upper_limit, n))
