import math
import random
from sympy import isprime

def euclid(one_number, two_number):
    r = [one_number, two_number]
    x = [1, 0]
    y = [0, 1]
    q = [0]
    i = 1
    while True:
        r.append(r[i - 1] % r[i])
        q.append(r[i - 1] // r[i])
        if r[i + 1] == 0:
            d = r[i]
            x = x[i]
            y = y[i]
            break
        x.append(x[i - 1] - q[i] * x[i])
        y.append(y[i - 1] - q[i] * y[i])
        i += 1
    return d, x, y


def solving(one_number, two_number, m):
    one_number, two_number = one_number % m, two_number % m
    from math import gcd
    d = gcd(m, one_number)
    if two_number % d != 0:
        return
    a_new, b_new, m_new = one_number // d, two_number // d, m // d
    d_new, q, r = euclid(a_new, m_new)
    q, r = q % m, r % m
    x0 = (b_new * q) % m_new
    for j in range(d):
        yield x0 + m_new * j


def f_function(y, g, h, m):
    if y <= m // 3:
        return (h * y) % m
    elif m // 3 < y < (2 * m) // 3:
        return pow(y, 2, m)
    else:
        return (g * y) % m


def a_function(y, a, m):
    if y <= m // 3:
        return (a + 1) % (m - 1)
    elif m // 3 < y <= 2 * m // 3:
        return (2 * a) % (m - 1)
    elif 2 * m // 3 < y:
        return a % (m - 1)


def b_function(y, b, m):
    if y <= m // 3:
        return b % (m - 1)
    elif m // 3 < y <= 2 * m // 3:
        return (2 * b) % (m - 1)
    elif 2 * m // 3 < y:
        return (b + 1) % (m - 1)


def next_elements(y, a, b, h, g, m):
    new_y = f_function(y, g, h, m)
    new_a = a_function(y, a, m)
    new_b = b_function(y, b, m)
    return new_y, new_a, new_b


def p_pollard_method(g, m, h, epsilon):
    t = int(math.sqrt(2*m*math.log(1/epsilon))) + 1
    while True:
        i = 1
        s = random.randint(0, m - 2)
        y0, a0, b0 = next_elements(pow(g, s, m), s, 0, h, g, m)
        y1, a1, b1 = next_elements(y0, a0, b0, h, g, m)
        while True:
            y0, a0, b0 = next_elements(y0, a0, b0, h, g, m)
            y1, a1, b1 = next_elements(*(next_elements(y1, a1, b1, h, g, m)), h, g, m)
            if y0 != y1:
                if i >= t:
                    return None
                i += 1
            else:
                new_b = (b0 - b1) % (m - 1)
                new_a = (a1 - a0) % (m - 1)
                d = math.gcd(new_a, m - 1)
                if d > int(math.sqrt(m - 1)):
                    break
                for x in solving(new_a, new_b, m - 1):
                    if pow(g, x, m) == h:
                        return x
                break


def main():
    g = int(input("Образующий элемент конечной циклической группы G: "))
    m = int(input("Порядок конечной циклической группы G: "))
    h = int(input("Элемент из G: "))
    epsilon = float(input("Значение epsilon: "))
    epsilon = 0.01
    if not isprime(m):
        print("Введено некорректное значение порядка!")
        exit(0)
    if not 0 <= h <= m - 1:
        print("Введено некорректное значение h!")
        exit(0)
    if not 0 < epsilon <= 1:
        print("Введено некорректное значение элемента группы!")
        exit(0)
    x = p_pollard_method(g, m, h, epsilon)
    if x is None:
        print("Вычислить x не удалось!")
        exit(0)
    print("Значение x = {}".format(x))

if __name__ == '__main__':
    main()
