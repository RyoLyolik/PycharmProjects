import math

def f(x): # монотонная функция
    return x**3-math.log2(x)
n = int(input())
l, r = 1, n

for i in range(100): # вещественный бинпоиск
    m = (l + r) / 2
    if f(m) > n:
        r = m
    else:
        l = m
print(l, f(l))