# task 1
# https://planetcalc.ru/8456/?ysclid=m3esr2rkg2220698260
def continued_fraction(a, b):
	"""Вычисление цепной дроби и подходящих дробей для a и b."""
	P = [0, 1]
	Q = [1, 0]
	q_list = []
	i = 1

	print(f"a0 = {a}, a1 = {b}")

	while b != 0:
		q = a // b
		remainder = a % b
		print(f"a{i-1} = {a} = {b} * {q} + {remainder} = a{i} * q{i} + a{i+1}")
		q_list.append(q)
		
		P.append(q * P[-1] + P[-2])
		Q.append(q * Q[-1] + Q[-2])
		
		a, b = b, remainder
		i += 1

	gcd = a

	# Форматирование результата
	def format_answer(obj_name, elements):
		return f"{obj_name} = [{', '.join(map(str, elements))}]"

	answer = format_answer(f"{P[1]}/{Q[1]}", q_list)
	answer += "\nВыпишем подходящие дроби:\n(самостоятельная часть)\n"
	print(answer)

	return gcd, q_list, P, Q

def cont_frac(a, b):
	gcd, q_list, P, Q = continued_fraction(a, b)
	print(f"НОД(a, b) = {gcd}")
	print(f"q = {q_list}")
	print(f"P = {P}")
	print(f"Q = {Q}")
	print()

# Запуск программы
# task1(157,225)