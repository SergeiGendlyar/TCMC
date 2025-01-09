def jacobi(a, p):
    steps = []  # Список для хранения шагов
    if p <= 0 or p % 2 == 0:
        raise ValueError("p должно быть положительным нечетным")
    if a == 0:
        if p > 1:
            steps.append(f"Так как $a$ = 0, a $p$ > 1 то $\\left( \\frac{{{a}}}{{{p}}} \\right) = 0$")
            return 0, steps
        else:
            steps.append(f"Так как $a$ = 0, a $p$ < 1 то $\\left( \\frac{{{a}}}{{{p}}} \\right) = 1$")
            return 1, steps

    if a == 1:
        steps.append(f"Так как $a$ = 1 тогда получаем $\\left(\\frac{{{a}}}{{{p}}} \\right) = 1$")
        return 1, steps

    # Шаг 1: Приводим a по модулю p и приводим к симметричному представлению |b| < p/2
    steps.append(f"**Шаг 1:** На входе имеем $\\left( \\frac{{{a}}}{{{p}}} \\right)$.")
    steps.append(f"Заменяем $a$ = {a} на такое $b$, что $a$ ≡ $b (mod p)$ и $|b|$ < $(\\frac{{{p}}}{{{2}}})$\n")
    a1 = a
    a = a % p
    steps.append(f"$$ b = a (mod p) = {a1} (mod {p}) = {a}$$ ")
    if a >= p / 2:
        steps.append(f"Так как $b > \\frac{{{p}}}{{{2}}}$ то производим вычитания:")
        while a >= p / 2:
            steps.append(f"$$b = b - p = {a} - {p} = {a - p}$$")
            a -= p
    else:
        steps.append(f"$$|{a}| < \\frac{{{p}}}{{{2}}}$$")
    
    steps.append(f"Получим: $\\left( \\frac{{{a}}}{{{p}}} \\right)$")

    # Шаг 2: Если a отрицательное, выделяем множитель ((-1)/p)
    steps.append(f"**Шаг 2:** Если $b$ отрицательное, выделяем множитель $(\\frac{{{-1}}}{{p}})$.\nВ данном случае $b$ = {a}.")
    if a < 0:
        a = -a
        sign = -1 if p % 4 == 3 else 1
        steps.append(f"Тогда множитель будет равен ${sign}$, так как:\n $$p (mod 4) = {p} (mod 4) = {p % 4}$$")
    else:
        steps.append(f"Так как число $b = {a} > 0$ то:")
        sign = 1
    
    steps.append(f"Получим: ${sign} \\cdot (\\frac{{{a}}}{{{p}}})$")
    result = sign

    # Шаг 3: Если a четное, разбиваем на 2^t * a1 и вычисляем ((2)/p)
    steps.append(f"**Шаг 3:** Если $b$ четное, разбиваем на $2^t \\cdot a_{{1}}$ и вычисляем $( \\frac{{{2}}}{{p}} )$.")
    c = 0
    while a % 2 == 0:
        a //= 2
        c += 1
        if p % 8 in [3, 5]:
            result = -result
    steps.append(f"$$(\\frac {{2^{{{c}}} \\cdot {a}}}{{{p}}}) = {result} \\cdot \\left( \\frac{{{a}}}{{{p}}} \\right)$$")
    if result < 0:
        steps.append(f"$$p ≡ \\pm 3 (mod 8) \\to p mod 8 = {p % 8}$$")
    else:
        steps.append(f"$$p ≡ \\pm 1 (mod 8) \\to p mod 8 = {p % 8}$$")
    steps.append(f"Поэтому множитель: {result}")

    # Шаг 4: Применяем закон квадратичной взаимности Гаусса
    steps.append(f"**Шаг 4:** Применяем закон квадратичной взаимности Гаусса к символу $(\\frac{{{a}}}{{{p}}})$")
    steps.append(f"$$(\\frac{{p}}{{q}}) = (\\frac{{q}}{{p}}) \\cdot (-1)^{{(\\frac{{p - 1}}{{2}} \\cdot \\frac{{q - 1}}{{2}})}} \\to  $$")
    steps.append(f"$$(\\frac{{{a}}}{{{p}}}) = (\\frac{{{p}}}{{{a}}}) \\cdot (-1)^{{( \\frac{{{a - 1}}}{{{2}}} \\cdot \\frac{{{p - 1}}}{{2}})}} \\to  $$")
    steps.append(f"$$(\\frac{{{a}}}{{{p}}}) = (\\frac{{{p}}}{{{a}}}) \\cdot (-1)^{{({{{(a - 1) // 2}}} \\cdot {{{(p - 1) // 2}}})}} \n = (\\frac{{{p}}}{{{a}}}) \\cdot (-1)^{{{{{(a - 1) // 2 * (p - 1) // 2}}}}} \\to  $$")
    steps.append(f"$$(\\frac{{{a}}}{{{p}}}) = (\\frac{{{p}}}{{{a}}}) \\cdot {{{{{pow(-1, ((a - 1) // 2 * (p - 1) // 2))}}}}}$$")
    if a == 1:
        steps.append(f"Так как $a$ = 1 тогда получаем $\\left(\\frac{{{a}}}{{{p}}} \\right) = 1$")
        return result, steps
    if a % 4 == 3 and p % 4 == 3:
        result = -result

    # Рекурсивно вычисляем (p % a)/a
    #steps.append(f"**Рекурсия:** вычисление $\\left( \\frac{{{p} \\% {a}}}{{{a}}} \\right) = \\left( \\frac{{{p % a}}}{{{a}}} \\right)$")
    steps.append(f"**Рекурсия:** вычисление для $\\left( \\frac{{{p}}}{{{a}}} \\right)$")
    res, rec_steps = jacobi(p, a)
    steps.extend(rec_steps)
    return result * res, steps

def save_solution_to_md(a, p):
    # Вызов функции Jacobi
    result, steps = jacobi(a, p)

    # Формирование текста в Markdown
    markdown_text = f"<h3 style=\"text-align: center;\">Решение</h3>"
    markdown_text += "Шаги вычисления символа Якоби:\n\n"

    # Запись всех шагов
    for step in steps:
        markdown_text += f"{step}\n\n"

    markdown_text += f"**Ответ:** $\\left( \\frac{{{a}}}{{{p}}} \\right) = {result}$\n"
    return markdown_text



if __name__ == "__main__":
    # Пример использования
    a = 12314
    p = 23
    a = 88
    p = 347
    print("Якоби (a / p):")
    a = int(input("Укажите a: "))
    p = int(input("Укажите p: "))
    text = save_solution_to_md(a, p)
    with open("solution2.md", "w", encoding="UTF-8") as file:
        file.write(f"**Задание 2:** Вычислить символ Якоби $(\\frac{{{a}}}{{{p}}})$.\n")
        file.write(text)

    print("Решение записано в файл solution2.md")