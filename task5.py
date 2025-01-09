import math

def gelfond_shanks(a, b, m):
    r = int(math.sqrt(m - 1)) + 1
    str_data.append(f"Определим значение $r$.\n\n $$B = |Z_{{{m}}}^*| = {{{m}}} - 1 = {{{m - 1}}}$$\n\n $$r = [\\sqrt{{B}}] + 1 = {r} $$\n\n")
    str_data.append(f"Вычислим значения $a, a^2,...,a^{{r - 1}}$:\n\n")
    a_list = {}
    for k in range(1, r):
        str_data.append(f"$$a^{{{k}}} = {pow(a, k, m)}$$\n")
        a_list[pow(a, k, m)] = k
    lst_k = sorted([(k, pow(a, k, m)) for k in range(1, r)], key=lambda x: x[1])
    print(lst_k)
    print(a_list)
    str_data.append(f"Укажем упорядоченное множество пар $(k, a^k)$ по второму элементу список:\n\n $${lst_k}$$\n\n")
    a_1 = pow(a, -r, m)
    str_data.append(f"Вычислим значение $a_{{1}} = a^{{-r}}\\to {{{a}}}^{{{-r}}} = {pow(a, -r, m)} (mod {{{m}}})$\n\n")
    str_data.append(f"Для каждого $0 ≤ i ≤ r − 1$ вычислить $a^i_{{1}}$ и проверить, является ли элемент $a^i_{{1}}b$ второй координатой какойнибудь пары из упорядоченного множества. \n\n Если элемент такой был найден, то необходимо запомнить $k + ri$. Найдем их:\n")
    lst_res = []
    for i in range(r):
        val = pow(a_1, i, m) * b % m
        str_data.append(f"$$a_{{1}}^{{{i}}} = {pow(a_1, i, m) % m}$$\n\n")
        str_data.append(f"$$a_{{1}}^{{{i}}}b = {val}*{b} (mod {m}) = {val}$$\n\n")
        if val in a_list:
            k = a_list[val]
            str_data.append(f"Совпадение: $k = {k}, i = {i}, a^{{{k}}} = {val}$\n\n")
            lst_res.append(k + r * i)
    print(lst_res)
    if lst_res == []:
        str_data.append("Решение $x$ не найдено!!!")
    else:
        str_data.append(f"В результате получим следующее множество значений $k + ri$:\n\n $${lst_res}$$ \n\nИз него выберем минимальный элемент: ${min(lst_res)}$\n\n" )
        str_data.append(f"Проверим: $a^x = b (mod {{{m}}}) \\to {{{a}}}^{{{min(lst_res)}}} = {{{b}}} (mod {{{m}}})\\to{pow(a, min(lst_res), m)} = {b}$\n\n")
        str_data.append(f"Ответ: $x = {min(lst_res)} = \\log_{{{a}}}{{{b}}}$")
    return min(lst_res) if lst_res != [] else -1


if __name__ == "__main__":
    a = int(input("Укажите порождающий элемент a: "))
    m = int(input("Укажите модуль m (Z_m): "))
    # b = int(input(f"Укажите элемент b (0 <= b <= {m - 1}): "))
    b = 1
    str_data = []
    # a, b, m = 3, 9, 37
    # a, b, m = 3, 8, 16
    # print(gelfond_shanks(a, b, m))
    str_ = f"**Задание 5:** Определить порядок элемента $a = {a}$ в группе $Z_{{{m}}}$.\n Решение будет представлено с использованием алгоритма Гольфана-Шенкса. То есть поиск дискретного логарифма: $x = \\log{{_a}}{{b}}= \\log_{{{a}}}{{{b}}}$"
    str_data.append(f"<h3 style=\"text-align: center;\">Решение</h3>\n\n")
    print(gelfond_shanks(a, b, m))
    with open("solution5.md", "w", encoding="UTF-8") as f:
        f.write(str_)
        for line in str_data:
            f.write(line)
    
