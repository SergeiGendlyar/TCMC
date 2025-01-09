from sympy import isprime

def get_divisors(n):
	"""Возвращает список простых делителей числа n с учетом кратности."""
	divisors = []
	for i in range(2, (n // 2) + 1):
		while n % i == 0:
			divisors.append(i)
			n //= i
	return divisors

def to_subgroups(a, b, p):
	"""Основная функция для выполнения задачи."""
	p_min_1 = p - 1
	print(f"p = {p}")
	print(f"p - 1 = {p_min_1} = ", end="")

	# Получаем делители числа p - 1
	divisors = get_divisors(p_min_1)
	divs = set(divisors)
	mi = []
	fl = False

	# Выводим факторизацию p - 1
	for div in divs:
		if isprime(div):
			if fl:
				print(" * ", end="")
			cnt = divisors.count(div)
			mi.append(div ** cnt)
			print(f"{div}^{cnt}", end="")
			fl = True

	print()

	# Поиск образующего элемента
	for div in divs:
		is_ord = True
		order = div
		for div1 in divs:
			if isprime(div1):
				test = pow(div, p_min_1 // div1, p)
				if test == 1:
					print(f"{div} не является образующим, так как {div}^{p_min_1 // div1} % {p} = 1")
					is_ord = False
					break
				print(f"{div}^{p_min_1 // div1} = {div}^{p_min_1 // div1} = {test} != 1 (mod {p})")

		if is_ord:
			print(f" => a = {order} - образующий.")
			print(f"Z*{p} = 〈{order}〉.")
			print(f"|Z*{p}| = {p_min_1} = {mi[0]} * {mi[1]}")
			break

	print(f"Z*{p} содержит подгруппы Gi = 〈ai〉 порядка {mi[0]} и {mi[1]} для a1 = {mi[0]}, a2 = {mi[1]}")
	print(f"При этом x ≡ x1 (mod {mi[0]}) x ≡ x2 (mod {mi[1]})")
	print(f"где x1, x2: ({mi[0]}^{mi[1]})^x1 = {b}^{mi[1]} (mod {p})")
	print(f"	 ({mi[0]}^{mi[0]})^x1 = {b}^{mi[0]} (mod {p}) <= >")
	print(f"	<=> {order}^x1 = {pow(b, mi[1], p)} (mod {p})")
	print(f"		{order}^x2 = {pow(b, mi[0], p)} (mod {p})")
	print("Решим систему.")
	print("Найдем x1... дальше самостоятельно")

to_subgroups(2, 8, 13)