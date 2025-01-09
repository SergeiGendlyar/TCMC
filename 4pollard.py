from math import sqrt, log10, gcd
import random

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


def poly(coef, x):
    ans = 0
    for n,c in enumerate(coef):
        ans += c*x**n
    return ans


def p_pollard(n, f, eps):
    T = int(sqrt(2 * sqrt(n) * log10(1 / eps))) + 1
    x = list()
    a = random.randint(1, n)
    i = 0
    while i < T:
        a = poly(f, a) % n
        x.append(a)
        for k in range(i):
            d = gcd((x[i] - x[k]) % n, n)
            if 1 < d < n:
                return d
            elif d == n:
                return None
            elif d == 1:
                continue
        i += 1


if __name__ == '__main__':
    print("Число n = ", end='')
    n = int(input())
    if n < 0 or miller_rabin(n, 5):
        print("Введено неправильное значение числа n")
        exit()
    eps = float(input("Введите значение eps\n"))
    if eps < 0 or eps > 1:
        print("Введено неправильное значение eps\n")
    print("Функция f, задаваемая коэффициентами = ", end='')
    f = list(map(int, input().split()))

    f.reverse()
    p = p_pollard(n, f, eps)

    if p is not None:
        print("Нетривиальный делитель p = {}".format(str(p)))
    else:
        print("Делитель не найден")
