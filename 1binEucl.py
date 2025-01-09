def binEvklid(a, b):
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a = a / 2
        b = b / 2
        g = 2 * g
    u = a
    v = b
    while u != 0:
        while u % 2 == 0:
            u = u / 2
        while v % 2 == 0:
            v = v / 2
        if u >= v:
            u = u - v
        else:
            v = v - u
    d = g * v
    return int(d)

def main():
    a = int(input("Введите первое число = \"a\"\n"))
    b = int(input("Введите второе число = \"b\" (0 < b <= a)\n"))
    if a < b or b < 0:
        print("Введите коректные значения")
        return 0
    else:
        print(binEvklid(a, b))

if __name__ == '__main__':
    main()
