def gcd(a,b): # НОД
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a,b): # НОК
    return a*b // gdc(a,b)
a, b = input().split()
a = int(a)
b = int(b)
print(gdc(a,b), lcm(a,b))