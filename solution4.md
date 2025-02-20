**Задание 4:** Решите следующую систему сравнений:
 $$
\begin{cases}
 x ≡ 5 (mod 10) \\x ≡ 7 (mod 13) \\x ≡ 3 (mod 9) \\\end{cases}
$$
Если для каждого $1 \leq j \leq k$ число $M_{j} = \frac{M}{m_j}$ и сравнение $M_jx ≡ a_j (mod m_j)$ имеет решение $z_j$, то решением системы линейных сравнений является остаток по модулю М числа:
 $$x = M_1z_1 + M_2z_2 +....+ M_kz_k$$
<h3 style="text-align: center;">Решение</h3>

Найдем $M$:

$$M = 10 * 13 * 9 = 1170$$

Найдем значения $M_{j}$ (Вычисление обратного элемента производится с помощью расширенного алгоритма Евклида):

$$M_{1} = \frac{10 * 13 * 9}{10} = 117 \to117z_{1} ≡ 5 (mod 10) \to 

z_{1} ≡ 5 * 117^{-1}(mod 10) \to$$ 

$$z_{1} ≡ 5 * 3 (mod 10) \to$$

$$z_{1} ≡ 5$$

$$M_{2} = \frac{10 * 13 * 9}{13} = 90 \to90z_{2} ≡ 7 (mod 13) \to 

z_{2} ≡ 7 * 90^{-1}(mod 13) \to$$ 

$$z_{2} ≡ 7 * -1 (mod 13) \to$$

$$z_{2} ≡ 6$$

$$M_{3} = \frac{10 * 13 * 9}{9} = 130 \to130z_{3} ≡ 3 (mod 9) \to 

z_{3} ≡ 3 * 130^{-1}(mod 9) \to$$ 

$$z_{3} ≡ 3 * -2 (mod 9) \to$$

$$z_{3} ≡ 3$$

$$x = 117 * 5 + 90 * 6 + 130 * 3 =345$$
Проверим при $x$ = 345:
$$
\begin{cases}
 x ≡ 5 (mod 10) \\x ≡ 7 (mod 13) \\x ≡ 3 (mod 9) \\\end{cases}
$$
$$\to$$

$$
\begin{cases}
 345 ≡ 5 (mod 10) \\345 ≡ 7 (mod 13) \\345 ≡ 3 (mod 9) \\\end{cases}
$$
$$\to$$

$$5 = 5$$
$$7 = 7$$
$$3 = 3$$
