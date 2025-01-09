def KToO(a, b, number):
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1

    while a % b != 0:
        q = a // b
        tmp_b = b
        b = a % b
        a = tmp_b
        tmp_x = x1
        x1 = x0 - q*x1
        x0 = tmp_x
        tmp_y = y1
        y1 = y0 - q * y1
        y0 = tmp_y

    if number == 0:
        return b
    elif number == 1:
        return x1
    elif number == 2:
        return y1

def KTO(u, m):
    k = len(m)

    M = 1
    for i in range(k):
        M *= m[i]

    c = [M // m[i] for i in range(k)]
    d = []

    for i in range(k):
        if c[i] >= m[i]:
            d.append(KToO(c[i], m[i], 1))
        else:
            d.append(KToO(m[i], c[i], 2))

    U = 0
    for i in range(k):
        U += c[i] * d[i] * u[i]
        U %= M

    return U

def main():
    u = list(map(int, input("Введите u1, u2, ... , uk: ").split()))
    m = list(map(int, input("Введите m1, m2, ... , mk: ").split()))
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if KToO(m[i], m[j], 0) != 1:
                print("Ошибка в веденных параметрах: числа m" + str(i) + " m" + str(j) + " не взаимно просты")
                exit(0)

    U = KTO(u, m)
    print("Ответ: " + str(U))

if __name__ == '__main__':
    main()
