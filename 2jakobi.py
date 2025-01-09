def rasEvklid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = rasEvklid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def jacobi(a, n):
    if (rasEvklid(a, n)[0] != 1):
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

def main():
    a = int(input("Введите коэффициент а = \n"))
    p = int(input("Введите коэффициент p = \n"))
    print(f'Символ Лежандра = {jacobi(a, p)}')

if __name__ == '__main__':
    main()
