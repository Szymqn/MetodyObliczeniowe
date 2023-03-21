def Lagrange(values, pos, n):
    idx = len(pos)
    result = 0

    for i in range(idx):
        L = 1
        for j in range(idx):
            if j != i:
                L *= (n - pos[j]) / (pos[i] - pos[j])

        result += L * values[i]

    print(result)


if __name__ == '__main__':
    # values = [7, 9, 18]
    # pos = [1, 2, 3]
    # n = 1.5

    # values = [975, 433, 7, -1, 235]
    # pos = [-5, -4, -1, 3, 5]
    # n = 2

    # Sprawozdanie result: -1
    values = [-1011, -73, 1, -21, -523]
    pos = [-4, -2, 0, 2, 4]
    n = 1

    Lagrange(values, pos, n)
