def legandr(a, p):
    if a == 1:
        return 1
    if a % 2 == 0:
        return legandr(a // 2, p) * (-1) ** ((p ** 2 - 1) // 8)
    if a % 2 == 1 and a != 1:
        return legandr(p % a, a) * (-1) ** ((a - 1) * ((p - 1) // 4))

def main():
    a = int(input("Введите коэффициент а = \n"))
    p = int(input("Введите коэффициент p = \n"))
    print(f'Символ Лежандра = {legandr(a, p)}')

if __name__ == '__main__':
    main()
