# sprawozdanie nr. 0: (-4, -1011) (-2, -73) (0, 1) (2, -21) (4, -523)

# except L: 0.375, 0.75, -0.125
def Lagrange(values, pos, n):
    idx = len(values)+1
    result = 0

    for i in range(1, idx):
        L = 1
        for j in range(1, idx):
            if i != j:
                L *= (n-j)/(i-j)

        print(f'L: {L}')
        result += values[i-1]*L

    print('Result:', result)


if __name__ == '__main__':
    values = [7, 9, 18]
    pos = [1, 2, 3]
    n = 1.5

    Lagrange(values, pos, n)
