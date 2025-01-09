import numpy as np

def euclid_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclid_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_multiplicative_inverse(a, m):
    g, x, _ = euclid_extended(a, m)
    if g != 1:
        return None
    else:
        return (x % m + m) % m

def gauss(matrix, m):
    size = len(matrix)
    matrix = [[a % m for a in row] for row in matrix]
    for i in range(size - 1):
        diagonal_element = matrix[i][i]
        inverse = modular_multiplicative_inverse(diagonal_element, m)
        matrix[i] = [(a % m * inverse) % m for a in matrix[i]]
        # print(matrix[i])
        for j in range(i + 1, size):
            subrow = [(a % m * matrix[j][i] % m) % m for a in matrix[i]]
            matrix[j] = [(a - s) % m for a, s in zip(matrix[j], subrow)]
    return matrix


def ext_euclid(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = ext_euclid(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x

def Gauss(A, m):
    for i in range(len(A)):
        g, a_, y = ext_euclid(A[i][i], m)
        A[i] = (A[i] % m * a_) % m
        # print(A[i])
        if i != len(A) - 1:
            for j in range(i + 1, len(A)):
                A[j] -= (A[i] % m * A[j][i] % m) % m
                A[j] = A[j] % m
    return A

def main():
    print("Введите количество строк в матрице =", end =' ')
    n = int(input())
    print("Введите количество столбцов в матрице =", end =' ')
    m = int(input())
    print("Введите матрицу =", end =' ')
    A = []
    for i in range(n):
        a = list(map(int, input().split()))
        A.append(a)
    print(A)
    print("Введите модуль =", end =' ')
    m = int(input())
    print(Gauss(np.array(A), m))

if __name__ == '__main__':
    main()
