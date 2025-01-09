#Расширенный алгоритм Евклида
def rasEvklid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = rasEvklid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def cepnya(a_1, a_2):
    q = []
    while (a_1 % a_2 != 0):
        q.append(a_1//a_2)
        a_1 %= a_2
        a_1, a_2 = a_2, a_1
    q.append(a_1 // a_2)
    return q

def diofant(a, b, c):
    gcd, x, y = rasEvklid(a, b)
    p, q = [0, 1], [1, 0]
    q_chain = cepnya(a, b)

    for i in range(len(q_chain)):
        p.append(q_chain[i] * p[i + 1] + p[i])
        q.append(q_chain[i] * q[i + 1] + q[i])
    p = p[2:]
    q = q[2:]
    if c % gcd == 0:
        k = len(p)
        a /= gcd; b/= gcd; c /= gcd;
        x = int((-1) ** k * q[-2] * c + b)
        y = -1 * int((-1) ** k * p[-2] * c + a)
    return x, y

def main():
    a = int(input("Введите коэффициент а = \n"))
    b = int(input("Введите коэффициент b = \n"))
    c = int(input("Введите коэффициент c = \n"))
    print(f'x = {diofant(a, b, c)[0]} y = {diofant(a, b, c)[1]}')

if __name__ == '__main__':
    main()
