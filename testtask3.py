def format_matrix(matrix):
    """
    Форматирует матрицу в виде LaTeX для Markdown.
    :param matrix: Двумерный массив (список списков).
    :return: Строка с LaTeX разметкой для матрицы.
    """
    rows = [" & ".join(map(str, row)) for row in matrix]
    return "\\begin{bmatrix}\n" + "\\\\ \n".join(rows) + "\n\\end{bmatrix}"


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
	for vector in vectors:
		ss = len(vector)
		first_nonzero = next((i for i, x in enumerate(vector) if x != 0), None)
		if first_nonzero is not None:
			equation = f'x{first_nonzero + 1} = ' + ' + '.join(f'{coef}x{idx + 1}' for idx, coef in enumerate(vector[first_nonzero + 1:-1]) if coef != 0)
			if vector[-1] != 0:
				equation += ' + ' + str(vector[-1])
			print(equation)

def gauss_f(f, mtrx):
	# прямой ход метода Гаусса
	n = len(mtrx)
	m = len(mtrx[0])
	print('Исходная матрица системы: ')
	print(mtrx[0])
	print(mtrx[1])
	print(mtrx[2])
	print()
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
			return
		valid_rows.append(mtrx[i])
	# окончательное количество строк проверяется для вывода результата
	if len(valid_rows) == m - 1:
		print('Разрешенная матрица:')
		for i in range(len(valid_rows)):
			print(valid_rows[i])
		print()
		print_vector_equation(valid_rows)
		print('Система имеет единственное решение!\n')
	else:
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
		print('Система имеет бесконечное число решений!\n')
		arr = [i for i in range(m1 - 1)]
		indxs = []
		for i in range(n1):
			fnz2 = next((j for j in range(m1) if valid_rows[i][j] != 0), -1)
			indxs.append(fnz2)
		result = [x for x in arr if x not in indxs]
		print('Для получения частного решения, введите свободные коэффициенты: ')
		coef = []
		for i in result:
			tmp = []
			xi = int(input(f'x{i + 1} = '))
			tmp.append(xi)
			tmp.append(i)
			coef.append(tmp)
		print()
		res = []
		for i in range(len(valid_rows)):
			k = 0
			for j in range(len(coef)):
				k += coef[j][0] * valid_rows[i][coef[j][1]]
			k += valid_rows[i][-1]
			res.append(k % f)
		print('Частное решение: ')
		for c in coef:
			print(f'x{c[1] + 1} = {c[0]}')
		for i in range(len(valid_rows)):
			print(f'x{indxs[i] + 1} = {res[i]}')
		print()
	return


f = 5
mtrx = [[3, 2, 1, 1, 2],[2, 5, 2, 1, 3],[1, 0, 3, 2, 4]]
gauss_f(f, mtrx)

# f = 7
# mtrx = [[1, 0, -2, -4, 2],[2, -2, 0, -3, 1],[0, 2, -4, -5, 3]]
# gauss_f(f, mtrx)
