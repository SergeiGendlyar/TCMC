def Evklid(a, b):
    while a % b != 0:
        tmp = b
        b = a % b
        a = tmp
    return b

def main():
    a = int(input("Введите первое число = \"a\"\n"))
    b = int(input("Введите второе число = \"b\" (0 < b <= a)\n"))

    if a < b or b < 0:
        print("Введите коректные значения")
        return 0
    else:
        print(Evklid(a, b))
if __name__ == '__main__':
    main()
