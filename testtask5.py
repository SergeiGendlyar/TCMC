# task5
from sympy import mod_inverse
import math

def get_pairs(a, p, r):
	"""Возвращает список пар (k, a^k) для значений k от 1 до r-1."""
	pairs = []
	a_pow_k = a
	for k in range(1, r):
		pairs.append((k, a_pow_k))
		print(f"a^{k} = {a_pow_k}", end=", " if k != r - 1 else ".\n")
		a_pow_k = (a_pow_k * a) % p
	return sorted(pairs, key=lambda x: x[1])

def gelfond_shanks_log(a, b, p):
	"""Вычисление дискретного логарифма log_a(b) по модулю p методом Гельфонда-Шенкса."""
	# Шаг 1: Определяем r и формируем пары
	r = int(math.sqrt(p - 1)) + 1
	print(f"Шаг 1. B = |Z{p}| = {p - 1}, r = [sqrt(B)] + 1 = {r}.")
	print(f"	   a = {a},")

	# Получаем отсортированный список пар (k, a^k)
	pairs = get_pairs(a, p, r)
	print("	   Упорядочиваем по 2й координате: ", pairs)

	# Шаг 2: Вычисляем a^(-r) и ищем совпадения с b
	a_inv_r = mod_inverse(pow(a, r, p), p)
	print(f"Шаг 2. Для элемента a^-r = ({a}^{r})^-1 = {a_inv_r}")
	print("	   Вычисляем a_inv_r^i * b и проверяем совпадения со второй координатой пар:")

	a_inv_r_i = 1
	for i in range(r):
		candidate = (a_inv_r_i * b) % p
		print(f"	   a_inv_r^{i} * b = {candidate}", end="")
		for k, ak in pairs:
			if candidate == ak:
				result = k + r * i
				print(f" = a^{k}. => k = {k}, i = {i}.")
				print(f"	   => k + ri = {k} + {r}*{i} = {result} = log_{a}({b}) (mod {p}).")
				return result
		print(",")
		a_inv_r_i = (a_inv_r_i * a_inv_r) % p

	return None

gelfond_shanks_log(3, 36,37)

