from math import prod

def greek_ch(xi, mi):
	M = prod(mi)
	print("M =", " * ".join(map(str, mi)), "=", M)
	
	# Вычисляем значения Mi для каждого mi
	Mi = [M // m for m in mi]
	for i, (M_i, m) in enumerate(zip(Mi, mi)):
		print(f"M{i+1} = {M} / {m} = {M_i}")
	
	# Находим значения z для каждого i
	zi = []
	for i, (M_i, x, m) in enumerate(zip(Mi, xi, mi)):
		z = 1
		while (M_i * z) % m != x:
			z += 1
		zi.append(z)
		print(f"{M_i}x ≡ {x} (mod {m}) => z{i+1} = {z}")
	
	# Находим решение x по формуле Китайской теоремы об остатках
	x = sum(z * M_i % M for z, M_i in zip(zi, Mi)) % M

	# Печать промежуточных вычислений
	print("x = (", end="")
	for i, (z, M_i) in enumerate(zip(zi, Mi)):
		print(f"{z}*{M_i}", end=" + " if i != len(zi) - 1 else f") (mod {M}) = (")
	for i, (z, M_i) in enumerate(zip(zi, Mi)):
		print(f"{z * M_i}", end=" + " if i != len(zi) - 1 else f") (mod {M}) = ")
	print(x)

# Пример использования
xi = [5, 7, 3]  # значения xi
mi = [10, 13, 9]  # значения mi
greek_ch(xi, mi)
