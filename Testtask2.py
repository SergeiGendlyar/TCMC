# task2
def jacobi(a, p):
	if p <= 0 or p % 2 == 0:
		raise ValueError("p должно быть положительным нечетным простым числом")
	if a == 0:
		if p > 1:
			print(f"Шаг 4: ({a} / {p}) = 0")
			return 0
		else:
			print(f"Шаг 4: ({a} / {p}) = 1")
			return 1

	if a == 1:
		print(f"Шаг 4: ({a} / {p}) = 1")
		return 1

	# Шаг 1: Приводим a по модулю p и приводим к симметричному представлению |b| < p/2
	print(f"Шаг 1 (до коррекции): ({a} / {p})")
	a = a % p
	while a >= p / 2:
		a -= p
	print(f"Шаг 1 (коррекция): ({a} / {p})")

	# Шаг 2: Если a отрицательное, выделяем множитель ((-1)/p)
	if a < 0:
		a = -a
		sign = -1 if p % 4 == 3 else 1
	else:
		sign = 1
	print(f"Шаг 2: {sign} * ({a} / {p})")
	result = sign
	# Шаг 3: Если a четное, разбиваем на 2^t * a1 и вычисляем ((2)/p)
	c = 0
	while a % 2 == 0:
		a //= 2
		c += 1
		if p % 8 in [3, 5]:
			result = -result
	print(f"Шаг 3: (2^{c}*{a} / {p}) = {result} * ({a} / {p})")

	# Шаг 4: Применяем закон квадратичной взаимности Гаусса
	if a == 1:
		print(f"Шаг 4: ({a} / {p}) = {result}")
		return result
	if a % 4 == 3 and p % 4 == 3:
		result = -result
		print(f"Шаг 4: ({a} / {p}) = {result}")

	# Рекурсивно вычисляем (p % a)/a
	print(f"Рекурсия: вычисление ({p} % {a} / {a})")
	return result * jacobi(p % a, a)

# https://www.walter-fendt.de/html5/men/legendresymbol_en.htm

print(jacobi(532,2739))
print(jacobi(1080,2945))

