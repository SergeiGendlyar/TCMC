#Расширенный алгоритм Евклида
def rasEvklid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = rasEvklid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

#1 способ
def reverse_element(a, m):
    return(pow(a, -1, m))

#2 способ
def reverse_element_2(a, m):
    gcd, x, y = rasEvklid(a, m)
    if gcd != 1:
        print("Нет обратного элемента")
    else:
        count = abs(x) // m + 1
        x = (x + count * m) % m
        return(x)


def main():
    n = int(input("Число n = \n"))
    p = int(input("Модуль p = \n"))
    print(f'Первый способ: Обратный элемент к {n} = {reverse_element(n,p)}')
    # reverse_element_2(n,p)
    print(f'Второй способ: Обратный элемент к {n} = {reverse_element_2(n,p)}')

if __name__ == '__main__':
    main()
