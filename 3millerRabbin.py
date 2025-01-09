from random import randint

def Miller_Rabin(n):
    s = 0
    n_test = n -1
    while(n_test % 2 == 0):
        s += 1
        n_test //= 2
    r = n_test
    a = randint(2, n - 2)
    y = a ** r % n
    j = 1
    if y != 1 and y != n - 1:
        while j <= s - 1 and y != n - 1:
            y = y ** 2 % n
            if y == 1:
                return f'Число {n} составное'
            j += 1
    if y != n - 1:
        return f'Число {n} составное'
    return f'Число {n}, веротяно, простое'

def main():
    p = int(input("Введите число = \n"))
    print(Miller_Rabin(p))

if __name__ == '__main__':
    main()
