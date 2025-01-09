from math import log, gcd
from random import randint
def miller_rabin(p, k):
    s = p - 1
    m = 0
    while s % 2 == 0:
        s //= 2
        m += 1
    i = 0
    while i <= k:
        from random import randint
        a = randint(2, p - 2)
        from math import gcd
        while gcd(a, p) != 1:
            a = randint(2, p - 2)
        b = pow(a, s, p)
        if b == 1:
            continue
        if b == p - 1:
            i += 1
            continue
        flag = False
        for l in range(1, m):
            c = pow(a, (s * pow(2, l)), p)
            if c == p - 1:
                flag = True
                break
        if flag:
            i += 1
            continue
        else:
            return False
    return True

def prime_numbers_less_than_B(B):
    primes = []
    for num in range(2, B + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def base(B, n):
    q = prime_numbers_less_than_B(B)
    T = 1
    for i in q:
        T = pow(T, i ** int(log(n) / log(i)))
    return T


def p_1_pollard(n):
    B = int(input("Введите число B: "))
    q = prime_numbers_less_than_B(B)
    print(B)
    print(q)
    T = base(B, n)
    check = 0
    while True:
        a = randint(2, n - 1)
        check += 1
        d = gcd(a, n)
        if d == 1:
            b = (pow(a, T) - 1) % n
            n1 = gcd(b, n)
            if (n1 > 1) and (n1 < n):
                return n1
                break
            if n1 == n:
                if check != 2:
                    continue
                else:
                    B -= 1
                    q = prime_numbers_less_than_B(B)
                    print(B)
                    print(q)
                    T = base(B, n)
                    check = 0
            if n1 == 1:
                B += 1
                q = prime_numbers_less_than_B(B)
                print(B)
                print(q)
                T = base(B, n)





if __name__ == '__main__':
    print("Введите число n = ", end='')
    n = int(input())
    if n < 0:
        print("Введено отрицательное число n")
        exit()
    elif miller_rabin(n, 5):
        print("Введено простое число n")
        exit()
    p = p_1_pollard(n)
    if p is not None:
        print("Нетривиальный делитель p = {} числа n".format(str(p), str(n)))
    else:
        print("Делитель не найден")
