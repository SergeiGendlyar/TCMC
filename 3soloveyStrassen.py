from random import randint

def euclid_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclid_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def jacobi(a, n):
    if (euclid_extended(a, n)[0] != 1):
        return 0
    if (a < 0):
        return jacobi(-a, n) * -1 ** ((n - 1) // 2)
    if a % 2 == 0:
        return jacobi(a // 2, n) * (-1) ** ((n ** 2 - 1) // 8)
    if a == 1:
        return 1
    if (a < n):
        return jacobi(n, a) * (-1) ** ((a - 1) * ((n - 1) // 4))
    return jacobi(a % n, n)

def Solovey_Strassen(n):
    a = randint(2, n - 2)
    r = a ** ((n-1) // 2) % n
    if r!= 1 and r != n-1:
        return f'Число {n} составное'
    s = jacobi(a, n)
    if r % n == s % n:
        return f'Число {n}, вероятно, простое'
    else:
        return f'Число {n} составное'

def main():
    p = int(input("Введите число = \n"))
    print(Solovey_Strassen(p))

if __name__ == '__main__':
    main()
