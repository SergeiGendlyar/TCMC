def rasEvklid(a, b):
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
    return b, x1, y1

def main():
    a = int(input("Введите первое число = \"a\"\n"))
    b = int(input("Введите второе число = \"b\" (0 < b <= a)\n"))
    if a < b or b < 0:
        print("Введите коректные значения")
        return 0
    else:
        print(rasEvklid(a, b))

if __name__ == '__main__':
    main()
