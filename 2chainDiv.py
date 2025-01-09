def cepnya(a_1, a_2):
    q = []
    while (a_1 % a_2 != 0):
        q.append(a_1//a_2)
        a_1 %= a_2
        a_1, a_2 = a_2, a_1
    q.append(a_1 // a_2)
    return q

def main():
    n = int(input("Введите числитель дроби = \n"))
    p = int(input("Введите Знаменатель дроби = \n"))
    print(f'Выводим последовательной цепной дроби {cepnya(n,p)}')

if __name__ == '__main__':
    main()
