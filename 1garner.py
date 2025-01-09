def garner(a, b, number):
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

def garner_method(a, m):
    k = len(m)
    c = [0]
    for i in range(1, k):
        c.append(1)
        for j in range(0, i):
            if m[j] >= m[i]:
                u = garner(m[j], m[i], 1)
            else:
                u = garner(m[i], m[j], 2)
            c[i] = (u * c[i]) % m[i]
    u = a[0]
    x = u
    for i in range(1, k):
        u = ((a[i] - x) * c[i]) % m[i]
        from numpy import prod
        x = x + u * prod(m[:i])

    return x

def main():
    a = list(map(int, input("Введите a1, a2, ... , ak: ").split()))
    m = list(map(int, input("Введите m1, m2, ... , mk: ").split()))
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if garner(m[i], m[j], 0) != 1:
                print("Ошибка в веденных параметрах: числа m" + str(i) + " m" +
                      str(j) + " не взаимно просты")
                exit(0)

    U = garner_method(a, m)

    print("Ответ: " + str(U))

if __name__ == '__main__':
    main()
