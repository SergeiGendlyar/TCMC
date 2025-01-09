def chain_div(a, b):
    res = []
    steps = []
    while b:
        div_ = a // b
        remainder = a % b
        steps.append((a, b, div_, remainder))  # Сохранение промежуточных значений
        res.append(div_)
        a, b = b, remainder
    return res, steps


def build_fraction_chain(steps):
    """
    Строит представление цепной дроби в виде вложенных дробей.
    """
    fractions = []
    for i in reversed(range(len(steps))):
        q = steps[i][2]
        if i == len(steps) - 1:
            fractions.append(f"{q}")
        else:
            fractions.append(f"{q} + \\frac{{1}}{{{fractions.pop()}}}")
    return fractions[0]


def format_chain_fraction(a, b, steps):
    """
    Формирует текст с вычислениями цепной дроби, включая разложения дробей.
    """
    markdown_text = f"<h3 style=\"text-align: center;\">Решение</h3>\n\nРассмотрим рациональное число $r = \\frac{{{a}}}{{{b}}}$.\n\n"
    markdown_text += "Для представления числа в виде цепной дроби используем алгоритм Евклида:\n\n"
    arr_qi = []
    for i, (a_i, b_i, q_i, r_i) in enumerate(steps):
        arr_qi.append(f"q_{{{i + 1}}}")
        # Основной шаг
        markdown_text += (
            f"$$a_{{{i}}} = {a_i}, \\quad b_{{{i}}} = {b_i}, \\quad "
            f"q_{{{i + 1}}} = {q_i}, \\quad r_{{{i + 1}}} = {r_i}$$\n\n"
        )
        markdown_text += (
            f"$$a_{{{i}}} = b_{{{i}}} \\cdot q_{{{i + 1}}} + r_{{{i + 1}}} \\quad \\Rightarrow \\quad "
            f"{a_i} = {b_i} \\cdot {q_i} + {r_i}$$\n\n"
        )

        # Дополнительное разложение дробей
        if b_i != 0:
            markdown_text += (
                f"$$\\frac{{a_{{{i}}}}}{{b_{{{i}}}}} = \\frac{{{a_i}}}{{{b_i}}} = "
                f"{q_i} + \\frac{{{r_i}}}{{{b_i}}}$$\n\n"
            )

    chain = "; ".join(map(str, [step[2] for step in steps]))
    q_chain = "; ".join(map(str, arr_qi))
    markdown_text += f"Следовательно, рациональное число $r = \\frac{{{a}}}{{{b}}}$ можно записать в виде цепной дроби: $[{q_chain}]$ = $[{chain}]$.\n\n"

    # Формирование вложенной дроби
    fraction_repr = build_fraction_chain(steps)
    markdown_text += f"Таким образом:\n\n"
    markdown_text += f"$$r = {fraction_repr}$$\n\n"

    return markdown_text


def suitable_fractions(a, b):
    """
    Вычисление подходящих дробей для цепной дроби.
    """
    steps_f = []
    P = [0, 1]
    Q = [1, 0]
    chain = []
    
    while b:
        q = a // b
        chain.append(q)
        steps_f.append((q, P[-1], Q[-1], P[-2], Q[-2]))
        P.append(q * P[-1] + P[-2])
        Q.append(q * Q[-1] + Q[-2])
        a, b = b, a % b
    return P, Q, chain, steps_f


def format_suitable_fractions(P, Q, chain):
    """
    Формирует текст с вычислениями подходящих дробей в Markdown формате.
    """
    markdown_text = (
"""Найдем для r числители и знаменатели подходящих дробей. Для этого составим таблицу с использованием следующих формул:\n
$$ P_{i} = q_{i} P_{i-1} + P_{i-2}, \quad Q_{i} = q_{i} Q_{i-1} + Q_{i-2} $$\n"""

    )
    markdown_text += """<div style="display: flex; justify-content: center;">\n\n"""
    markdown_text += "| $i$ | $q_i$ | $P_i$ | $Q_i$ |\n"
    markdown_text += "|---|---|---|---|\n"
    for i, (pi, qi) in enumerate(zip(P, Q)):
        qi_val = chain[i - 2] if i >= 2 else "–"
        markdown_text += f"| {i - 1} | {qi_val} | {pi} | {qi} |\n"
    
    markdown_text += """\n</div>"""

    return markdown_text


if __name__ == "__main__":
    # Ввод данных
    print("Укажите дробь (a / b):")
    a = int(input("a = "))
    b = int(input("b = "))

    # Заголовок задачи
    task_text = f"**Задание 1**: Представить рациональное число $r = \\frac{{{a}}}{{{b}}}$ в виде непрерывной дроби и выписать все её подходящие дроби."

    # Вычисления цепной дроби
    chain, steps = chain_div(a, b)
    solution_text = format_chain_fraction(a, b, steps)

    # Вычисления подходящих дробей
    P, Q, chain, steps_f = suitable_fractions(a, b)
    fractions_table = format_suitable_fractions(P, Q, chain)
    print(steps_f)

    # Запись в Markdown файл
    with open("solution1.md", "w", encoding="UTF-8") as file:
        file.write(task_text + "\n\n")
        file.write(solution_text + "\n")
        file.write(fractions_table + "\n\n")
        file.write(f"$$ P_{{{-1}}} = {0}, P_{{{0}}} = {1}, Q_{{{-1}}} = {1}, P_{{{0}}} = {0}$$\n") 
        for i, (q, P1, Q1, P2, Q2) in enumerate(steps_f):
            i = i + 1
            Pi = f"$$ P_{{{i}}} = q_{{{i}}}P_{{{i-1}}} + P_{{{i-2}}} = {q} \cdot {P1} + {P2} = {q * P1 + P2} , \quad "
            Qi = f"Q_{{{i}}} = q_{{{i}}}Q_{{{i-1}}} + Q_{{{i-2}}} = {q} \cdot {Q1} + {Q2} = {q * Q1 + Q2} $$\n"
            file.write(Pi + Qi + "\n")

    print("Решение записано в файл solution1.md")
