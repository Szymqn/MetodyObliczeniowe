# przykład nr.1
def integral(x):
    return x ** 2


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
    lower_limit = 1
    upper_limit = 4
    n = 3

    print(f"Wynik dla n = {n}:", trapeze_method(integral, lower_limit, upper_limit, n))
