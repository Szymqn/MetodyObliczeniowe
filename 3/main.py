def Lagrange(xi, fi, x):
    idx = len(fi)
    result = 0

    for i in range(idx):
        temp = 1
        for j in range(idx):
            if j != i:
                temp *= (x - xi[j]) / (xi[i] - xi[j])

        result += temp * fi[i]

    return result


if __name__ == '__main__':
    xi = [-4, -2, 0, 2, 4]
    fi = [-1011, -73, 1, -21, -523]
    x = 1

    print(f"Wynik dla x = {x}:", Lagrange(xi, fi, x))
