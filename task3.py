from copy import deepcopy

str_data = []

def format_matrix(matrix):
    """
    Форматирует матрицу в виде LaTeX для Markdown.
    :param matrix: Двумерный массив (список списков).
    :return: Строка с LaTeX разметкой для матрицы.
    """
    rows = [" & ".join(map(str, row)) for row in matrix]
    return "$$\n\\begin{bmatrix}\n" + "\\\\ \n".join(rows) + "\n\\end{bmatrix}\n$$\n"

def format_matrix_to_system(matrix):
    rows_str_matrix = "$$\n\\begin{cases}\n"
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[0])):
            if len(matrix[0]) - 1 == j:
                    row += f" = {matrix[i][j]}"
                    break
            if matrix[i][j] < 0:
                row += f"{matrix[i][j]}x_{{{j + 1}}}" 
            else:
                if j == 0 or j == len(matrix[0]) - 1:
                    row += f"{matrix[i][j]}x_{{{j + 1}}}"
                else:
                    row += f" + {matrix[i][j]}x_{{{j + 1}}}"
        rows_str_matrix += row + "\\\\" + "\n"
    rows_str_matrix += "\end{cases}\n$$\n"
    return rows_str_matrix


def save_chain_to_md(matrix_chain, filename, description="Преобразования"):
    """
    Сохраняет цепочку матриц в Markdown файл с описанием.
    :param matrix_chain: Список кортежей (описание, матрица).
    :param filename: Имя файла для записи.
    :param description: Текстовое описание перед цепочкой.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"### {description}:\n\n")
        for i, (step_desc, matrix) in enumerate(matrix_chain):
            if i > 0:
                file.write("$\\rightarrow$\n\n")  # Добавляем стрелку между матрицами
            file.write(f"{step_desc}\n\n")
            file.write(f"$${format_matrix(matrix)}$$\n\n")
            
# task3
def print_vector_equation(vectors):
    
    for vector in vectors:
        equation = ' + '.join(f'{coef}x{idx + 1}' for idx, coef in enumerate(vector[:-1]) if coef != 0)
        print(f'{equation} = {vector[-1]}')

def print_vector_equation_special(vectors):
    print(vectors)
    for vector in vectors:
        ss = len(vector)
        first_nonzero = next((i for i, x in enumerate(vector) if x != 0), None)
        if first_nonzero is not None:
            equation = f'x{first_nonzero + 1} = ' + ' + '.join(f'{coef}x{idx + 1}' for idx, coef in enumerate(vector[first_nonzero + 1:-1]) if coef != 0)
            if vector[-1] != 0:
                equation += ' + ' + str(vector[-1])
            print(equation)

def transform_system(matrix):
    res = "$$\n\\begin{cases}\n"
    for row in range(len(matrix)):
        res1 = ""
        flag = False
        for col in range(len(matrix[0]) - 1):
            el = matrix[row][col]
            if el != 0:
                if col == row:
                    res1 += f"x_{col + 1} = "
                else:
                    flag = True
                    if el < 0:
                        el = "" if el == -1 else f"{el}"
                        res1 += f"{el}x_{col + 1} "
                    else:
                        el = "" if el == 1 else f"{el}"
                        res1 += f"- {el}x_{col + 1} "
        if matrix[row][-1] < 0:
            res += f"{res1} {matrix[row][-1]}\\\\"
        else:
            if flag:
                res += f"{res1} + {matrix[row][-1]}\\\\"
            else:
                res += f"{res1} {matrix[row][-1]}\\\\"
    res += "\end{cases}\n$$\n"
    return res


def transform_system_2(matrix):
    res = "$$\n\\begin{cases}\n"
    for row in range(len(matrix)):
        res1 = ""
        for col in range(len(matrix[0]) - 1):
            el = matrix[row][col]
            if el != 0:
                if col == row:
                    res1 += f"x_{col + 1} = "
                else:
                    el = "" if el == 1 else f"{el}"
                    res1 += f"{el}x_{col + 1} + "
        res1 = res1[:-2]
        if matrix[row][-1] < 0:
            res += f"{res1} {matrix[row][-1]}\\\\"
        else:
            res += f"{res1} + {matrix[row][-1]}\\\\"
    res += "\end{cases}\n$$\n"
    return res


def gauss_f(f, mtrx):
    # прямой ход метода Гаусса
    n = len(mtrx)
    m = len(mtrx[0])
    print(format_matrix_to_system(mtrx))
    str_data.append(format_matrix_to_system(mtrx))
    print('Исходная матрица системы: ')
    for row in mtrx:
        print(row)
    print()

    str_data.append(f"<h3 style=\"text-align: center;\">Решение</h3>\n\n")
    str_data.append('Исходная матрица системы: \n' + format_matrix(mtrx))
    for row in range(len(mtrx)):
        for col in range(len(mtrx[0])):
            mtrx[row][col] = mtrx[row][col] % f
    str_data.append(f'Приведем матрицу к элементам поля $Z_{{{f}}}$: \n' + format_matrix(mtrx))
    str_data.append("Представим исходную систему в виде расширенной матрицы после чего преобразуем матрицу к треугольному виду с помощью Жордановых преобразований:\n " + format_matrix(mtrx))
    for i in range(n):
        # поиск ведущего ненулевого элемента
        col = next((c for c in range(m) if mtrx[i][c] != 0), m)
        if col == m:
            continue  # переход к следующей строке, если ведущий элемент не найден

        el = mtrx[i][col]
        inv = pow(el, -1, f)
        inv %= f  # приведение к положительному модулю
        if inv < 0:
            inv += f

        # приведение строки к виду с единицей на ведущем элементе
        for j in range(col, m):
            mtrx[i][j] = (mtrx[i][j] * inv) % f

        # обнуление других строк в том же столбце
        for u in range(n):
            if u != i:
                mul = -mtrx[u][col]
                if mul != 0:
                    for j in range(col, m):
                        mtrx[u][j] = (mtrx[u][j] + mul * mtrx[i][j]) % f
        print('Промежуточный этап. Жордановы преобразования: ')
        
        for i in range(len(mtrx)):
            print(mtrx[i])
        print()

        str_data.append(format_matrix(mtrx))

    # обратный ход метода Гаусса для проверки решений
    valid_rows = []  # список строк, которые нужно сохранить
    for i in range(n):
        fnz = next((j for j in range(m) if mtrx[i][j] != 0), -1)
        if fnz == -1:
            continue  # строка состоит из нулей, её пропускаем
        elif fnz == m - 1:
            print('Полученная матрица:', mtrx)
            print_vector_equation(mtrx)
            print('Не имеет решений!\n')
            str_data.append('Исходная система не имеет решений!\n')
            return
        valid_rows.append(mtrx[i])
    print("-----------------------------", valid_rows)
    # окончательное количество строк проверяется для вывода результата
    if len(valid_rows) == m - 1:
        print('Разрешенная матрица:')
        for i in range(len(valid_rows)):
            print(valid_rows[i])
        print()
        print_vector_equation(valid_rows)
        print('Система имеет единственное решение!\n')
        str_data.append(f'Система имеет единственное решение! Разрешенная система: \n {format_matrix_to_system(valid_rows)}\n')
        str_data.append(transform_system(valid_rows))
    else:
        str_data.append(f"Система имеет бесконечное число решений!\n {format_matrix_to_system(valid_rows)}\n")
        str_data.append(f"Выразим неизвестные коэффициенты (перенесем за равно переменные для дальнейших преобразований).\n")
        str_data.append(transform_system(valid_rows))
        # --------------------------------------
    


        # --------------------------------------
        print('Полученная матрица:')
        for i in range(len(valid_rows)):
            print(valid_rows[i])
        print()
        n1 = len(valid_rows)
        m1 = len(valid_rows[0])
        for i in range(n1):
            fnz1 = next((j for j in range(m1) if valid_rows[i][j] != 0), -1)
            for j in range(fnz1 + 1, m1 - 1):
                valid_rows[i][j] = (-valid_rows[i][j]) % f
        print_vector_equation_special(valid_rows)
        str_data.append(f"Приведем коэф. при неизвестных к элементам поля $Z_{f}$:\n")
        str_data.append(transform_system_2(valid_rows))
        print('Система имеет бесконечное число решений!\n')

        arr = [i for i in range(m1 - 1)]
        indxs = []
        for i in range(n1):
            fnz2 = next((j for j in range(m1) if valid_rows[i][j] != 0), -1)
            indxs.append(fnz2)
        print(indxs)
        result = [x for x in arr if x not in indxs]
        print("===============", result)
        print('Для получения частного решения, введите свободные коэффициенты: ')
        str_data.append('Для получения частного решения, укажем следующие свободные коэффициенты: ')
        coef = []
        buff = ""
        for i in result:
            tmp = []
            xi = int(input(f'x{i + 1} = ')) % f
            buff += f"$x_{{{i + 1}}} = {xi}$, "
            tmp.append(xi)
            tmp.append(i)
            coef.append(tmp)
        str_data.append(buff[:-2] + "\n\n")
        print(coef)
        res = []
        for i in range(len(valid_rows)):
            k = 0
            for j in range(len(coef)):
                k += coef[j][0] * valid_rows[i][coef[j][1]]
            k += valid_rows[i][-1]
            res.append(k % f)
        print('Частное решение: ')
        str_data.append(f"Частное решение:\n")
        for c in coef:
            str_data.append(f"$x_{{{c[1] + 1}}} = {c[0]}$\n")
            print(f'x{c[1] + 1} = {c[0]}')
        for i in range(len(valid_rows)):
            str_data.append(f"$x_{{{indxs[i] + 1}}} = {res[i]}$\n")
            print(f'x{indxs[i] + 1} = {res[i]}')
        print()
    return

if __name__ == "__main__":

    f = int(input("Укажите поле Z: "))
    n = int(input("Количество уравнений: "))
    print("Укажите коэф уравнения через пробел и свободные члены:")
    mtrx = []
    for i in range(n):
        data = list(map(int, input().split()))
        mtrx.append(data)
    print(mtrx)

    # f = 5
    # mtrx = [[1, 3, 1, 4, 2],[1, 0, 5, 1, 0],[3, 1, 0, 1, -3]]

    # f = 23
    # mtrx = [[2, 3, 7, -14], [3, 6, 10, 0], [2, 1, 4, -16]]

    # f = 7
    # mtrx = [[1, 0, -2, -4, 2],[2, -2, 0, -3, 1],[0, 2, -4, -5, 3]]

    mtrx_c = deepcopy(mtrx)
    gauss_f(f, mtrx)
    str_ = f"**Задание 3:** Найти общее и одно частное решение в поле $Z_{{{f}}}$ для следующей системы линейных уравнений:\n"
    with open("solution3.md", "w", encoding="UTF-8") as f:
        f.write(str_)
        for line in str_data:
            f.write(line)
    
    # gauss_f(f, mtrx)
