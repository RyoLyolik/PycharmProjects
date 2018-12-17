
def our_pow(x, a):
    if a == 0:
        return 1
    elif a % 2 == 0:
        return our_pow(x*x, a//2)
    else:
        return x * our_pow(x*x, a // 2)
print(our_pow(99,9))
print(99**9)