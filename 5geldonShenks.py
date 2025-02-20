import math
from sympy import isprime

def egcd(one_number, two_number):
    if one_number == 0:
        return two_number, 0, 1
    else:
        g, x, y = egcd(two_number % one_number, one_number)
        return g, y - (two_number // one_number) * x, x


def gelfond_shenks_method(g, b, h):
    r = int(math.sqrt(b)) + 1
    ga = [[a, pow(g, a, b)] for a in range(r)]
    ga.sort(key=lambda el: el[1])
    g, x, _ = egcd(g, b)
    if g == 1:
        g1 = x % b
    g1 = pow(g1, r, b)
    x = b + 1
    for i in range(r):
        gh = (pow(g1, i, b) * h) % b
        for element in ga:
            if element[1] == gh:
                x = min(x, element[0] + r * i)
            elif element[1] > gh:
                break
    return x


def main():
    g = int(input("Образующий элемент конечной циклической группы G: "))
    b = int(input("Порядок конечной циклической группы G: "))
    h = int(input("Элемент из G: "))
    if not isprime(b):
        print("Введено некорректное значение порядка!")
        exit(0)
    if not 0 <= h <= b - 1:
        print("Введено некорректное значение элемента группы!")
        exit(0)
    x = gelfond_shenks_method(g, b, h)
    print("Значение x = {}".format(x))


if __name__ == '__main__':
    main()
