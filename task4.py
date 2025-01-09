# Расширенный алгоритм Евклида
def gcd_xt(a, b):
    s0, t0 = 1, 0
    s1, t1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return s0, t0, a

# Нахождение произведения элеметов в массиве
def prod(list):
    s = "$$M = " + " * ".join(map(str, list))
    res = 1
    for val in list: 
        res *= val
    s += f" = {res}$$\n\n"
    str_data.append(s)
    return res

# Китайсткая теорема об остатках (система сравнений)
def china_theorem(params, moduls):
    str_data.append("Найдем $M$:\n\n")
    M = prod(moduls)
    u = 0
    pairs = []
    str_data.append("Найдем значения $M_{j}$ (Вычисление обратного элемента производится с помощью расширенного алгоритма Евклида):\n\n")
    for i, m in enumerate(moduls):
        mul = " * ".join(map(str, moduls))
        c = M // m
        str_ = f"$$M_{{{i + 1}}} = \\frac{{{mul}}}{{{m}}} = {c} \\to"
        d, _, _ = gcd_xt(c, m)
        str_ += f"{c}z_{{{i + 1}}} ≡ {params[i]} (mod {m}) \\to \n\n"
        str_ += f"z_{{{i + 1}}} ≡ {params[i]} * {c}^{{{-1}}}(mod {m}) \\to$$ \n\n"
        str_ += f"$$z_{{{i + 1}}} ≡ {params[i]} * {d} (mod {m}) \\to$$\n\n"
        str_ += f"$$z_{{{i + 1}}} ≡ {(params[i]) * d % m}$$\n\n"
        u += c * d * params[i]
        str_data.append(str_)
        pairs.append((c, (d * params[i]) % m))
    ss = "$$x = " + " + ".join(f"{c} * {d}" for c, d in pairs) + " =" + str(u % M) + "$$"
    str_data.append(ss )
    return u % M

def format_system(u, m):
    str_cases = "$$\n" + "\\begin{cases}\n "
    for u_, m_ in zip(u, m):
        str_cases += f"x ≡ {u_} (mod {m_}) \\\\"
    str_cases += "\end{cases}\n$$\n"
    return str_cases

def format_system_2(u, m, x):
    str_cases = "$$\n" + "\\begin{cases}\n "
    for u_, m_ in zip(u, m):
        str_cases += f"{x} ≡ {u_} (mod {m_}) \\\\"
    str_cases += "\end{cases}\n$$\n"
    return str_cases

def check(u, m, x):
    str_data.append(f"\nПроверим при $x$ = {x}:\n")
    str_data.append(format_system(u, m))
    str_data.append("$$\\to$$\n\n")
    str_data.append(format_system_2(u, m, x))
    str_data.append("$$\\to$$\n\n")
    for u_, m_ in zip(u, m):
        if x % m_ != u_ % m_:
            str_data.append(f"$${x % m_} != {u_ % m_}$$\n")
            str_data.append("Сравнение не решено!")
            break
        str_data.append(f"$${x % m_} = {u_ % m_}$$\n")


if __name__ == "__main__":
    str_data = []
    u = [5, 7, 3]
    m = [10, 13, 9]
    # u = [1, 3, 2]
    # m = [3, 5, 4]
    # u = [3, 2]
    # m = [4, 3]
    str_ = f"**Задание 4:** Решите следующую систему сравнений:\n " + format_system(u, m)
    str_ += "Если для каждого $1 \leq j \leq k$ число $M_{j} = \\frac{M}{m_j}$ и сравнение $M_jx ≡ a_j (mod m_j)$ имеет решение $z_j$, то решением системы линейных сравнений является остаток по модулю М числа:\n $$x = M_1z_1 + M_2z_2 +....+ M_kz_k$$\n"
    str_data.append(f"<h3 style=\"text-align: center;\">Решение</h3>\n\n")
    x = china_theorem(u, m)
    check(u, m, x)
    with open("solution4.md", "w", encoding="UTF-8") as f:
        f.write(str_)
        for line in str_data:
            f.write(line)
        