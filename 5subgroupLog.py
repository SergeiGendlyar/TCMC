import math
from sympy import isprime

# Расширенный алгоритм Евклида для нахождения решения сравнений
def gcd_xt(a, b):
    s0, t0 = 1, 0
    s1, t1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return a, s0, t0

# Нахождение произведения элеметов в массиве
def prod(list):
    res = 1
    for val in list: res *= val
    return res


# Китайсткая теорема об остатках (система сравнений)
def china_theorem(params, moduls):
    M = prod(moduls)
    u = 0
    for i, m in enumerate(moduls):
        c = M // m
        d, _, _ = gcd_xt(c, m)
        u += c * d * params[i]
    return u % M

# Нахождение диксретного алгоритма перебором
def discrete_log(base, value, mod):
    for x in range(mod):
        if pow(base, x, mod) == value:
            return x
    return None

# Проверка на то как раскладывается число m
def check_m_factorization(m):
    prime_power, p, n = is_prime_power(m)
    if prime_power:
        return True, p, n
    coprime_factors, m1, m2 = find_coprime_factors(m)
    if coprime_factors:
        return False, m1, m2
    return "No valid factorization found"

# Является ли заданное число m степенью простого числа
def is_prime_power(m):
    for p in range(2, int(math.sqrt(m)) + 1):
        if isprime(p):
            n = 1
            while p ** n <= m:
                if p ** n == m:
                    return True, p, n
                n += 1
    return False, None, None

# Разложение числа на его простые множители
def find_coprime_factors(m):
    for m1 in range(2, m // 2 + 1):
        if m % m1 == 0:
            m2 = m // m1
            if math.gcd(m1, m2) == 1:
                return True, m1, m2
    return False, None, None



# Вычисление дискретного логарифма через собственные подгруппы
def log_subgroups(g, h, m):
    m = m - 1
    flag, m1, m2 = check_m_factorization(m)
    if flag:
        x = discrete_log(g, h, m + 1)
        return x
    else:
        # print(g, m2, h, g ** m2 % (m + 1), h ** m2 % (m + 1), m + 1)
        # print(g, m1, h, g ** m1 % (m + 1), h ** m1 % (m + 1), m + 1)
        p = m + 1
        x_1 = discrete_log(g ** m2 % p, h ** m2 % p, p)
        x_2 = discrete_log(g ** m1 % p, h ** m1 % p, p)
        x = china_theorem([x_2, x_1], [m2, m1])
        return x

def input_data():
    g = input("Образующий элемент конечной циклической группы G: ").strip()
    h = input("Элемент из G: ").strip()
    m = input("Порядок конечной циклической группы G: ").strip()
    while not (g.isdigit() and h.isdigit() and m.isdigit()):
        g = input("g = ").strip()
        h = input("h = ").strip()
        m = input("m = ").strip()
    return int(g), int(h), int(m)

def main():
    try:
        g, h, m = input_data()
        x = log_subgroups(g, h, m)
        print("Ответ:", x)
        print(f"Проверка g ^ x = h (mod m) => {g} ^ {x} = {h} (mod {m}) => {pow(g, x, m)} = {h % m}")
    except Exception:
        print("Дискретный логарифм не найден!")


if __name__ == '__main__':
    main()