import numpy as np


def simple_iterations(A, b, epsilon, max_iterations):
    n = len(A)
    x = np.zeros(n)
    iterations = 0

    while True:
        x_new = np.zeros(n)
        for i in range(n):
            x_new[i] = b[i]
            for j in range(n):
                if j != i:
                    x_new[i] -= A[i][j] * x[j]
            x_new[i] /= A[i][i]

        if abs(x_new[0] - x[0]) < epsilon or iterations >= max_iterations:
            break

        x = x_new
        iterations += 1

    return x, iterations


if __name__ == '__main__':
    matrix = np.array([[3, 1, 2], [1, -4, 1], [1, 2, 3]])
    results = np.array([5, -7, 2])
    epsilon = 0.01
    max_iterations = 100

    result, iteration = simple_iterations(matrix, results, epsilon, max_iterations)
    print(f"Wynik dla epsilon = {epsilon} metodą iteracji prostych wynosi: {result}, po {iteration} iteracjach")
