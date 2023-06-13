from sys import exit
from sympy import symbols, diff


def bisection_method(f, epsilon, a, b):
    f_a = f(a)
    center = (a + b) / 2
    iteration = 0

    while abs(f(center)) >= epsilon:
        center = (a + b) / 2
        f_sr = f(center)
        if f_sr == 0:
            break
        elif f_sr * f_a < 0:
            b = center
        else:
            a = center
        iteration += 1

    return center, iteration


def statistic_method(f, f_1, f_2, epsilon, a, b):
    iteration = 0

    if f_1(a) * f_1(b) < 0 and f_2(a) * f_2(b) < 0:
        print("Warunki zbieżności nie są spełnione.")

    if f_2(a) * f(a) > 0:
        x0 = a
    else:
        x0 = b

    xn = x0
    while True:
        iteration += 1
        xni = xn - f(xn) / f_1(xn)
        if abs(f(xni)) < epsilon or abs(xni - xn) < epsilon:
            return xni, iteration
        xn = xni


def secant_method(f, f_2, epsilon, a, b):
    iteration = 1

    if f(a) >= 0 and f_2(a) >= 0:
        x0 = a
        xn = x0 - (f(x0) / (f(b) - f(x0))) * (b - x0)
        xne = lambda x: x0 - (f(x0) / (f(b) - f(x))) * (b - x)
    else:
        x0 = b
        xn = x0 - (f(x0) / (f(x0) - f(a))) * (x0 - a)
        xne = lambda x: x0 - (f(x0) / (f(x0) - f(x))) * (x0 - x)

    while abs(f(xn)) > epsilon:
        iteration += 1
        x0 = xn
        xn = xne(xn)

    return xn, iteration


if __name__ == '__main__':
    x = symbols('x')
    f = lambda x_val: x_val ** 2 + 4.1 * x_val - 9

    f_1 = diff(f(x), x)
    f_2 = diff(f_1, x)

    f_1_l = lambda x_val: f_1.evalf(subs={x: x_val})
    f_2_l = lambda x_val: f_2.evalf(subs={x: x_val})

    epsilon = 0.01
    a = -10
    b = -3

    if f(a) * f(b) < 0:
        bisection_result, bisection_iteration = bisection_method(f, epsilon, a, b)
        print(f"Wynik dla epsilon = {epsilon}, na przedziale [{a}, {b}], metodą bisekcji wynosi: {bisection_result}, po {bisection_iteration} iteracjach")

        statistic_result, statistic_iteration = statistic_method(f, f_1_l, f_2_l, epsilon, a, b)
        print(f"Wynik dla epsilon = {epsilon}, na przedziale [{a}, {b}], metodą stycznych wynosi: {statistic_result}, po {statistic_iteration} iteracjach")

        secant_result, secant_iteration = secant_method(f, f_2_l, epsilon, a, b)
        print(f"Wynik dla epsilon = {epsilon}, na przedziale [{a}, {b}], metodą siecznych wynosi: {secant_result}, po {secant_iteration} iteracjach")
    else:
        exit("Warunek konieczny f(a) * f(b) < 0, nie został spełniony")
