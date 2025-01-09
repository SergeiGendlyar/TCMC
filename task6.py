import math

def gelfond_shanks(a, b, m):
    r = int(math.sqrt(m - 1)) + 1
    a_list = {pow(a, k, m) : k for k in range(1, r)}
    a_1 = pow(a, -r, m)
    lst_res = []
    for i in range(r):
        val = pow(a_1, i, m) * b % m
        if val in a_list:
            k = a_list[val]
            lst_res.append(k + r * i)
    print(lst_res)
    return min(lst_res)

def main():
    math.log(2 ** 4, 23 ** 3)
    math.log(23 ** 3, 2 ** 4)


if __name__ == "__main__":
    a, b, m = 18, 17, 19
    print("============>", gelfond_shanks(a, b, m))
    str_data = []
    print("Вычислим x = log_a(b) в группе Z_n")
    a = int(input("Укажите основание логарифма a: "))
    b = int(input("Укажите показатель логарифма b: "))
    n = int(input("Укажите порядок группы n: "))

    main()
    str_ = f"**Задание 6:**  Вычислить $x = log_{{{a}}}{{{b}}}$ в группе $Z_{{{n}}}^*$ методом сведения к собственным подгруппам. "
    with open("solution6.md", "w", encoding="UTF-8") as f:
        f.write(str_)
        for line in str_data:
            f.write(line)
