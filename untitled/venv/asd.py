a = [2, 4,5,7,9,10,15,17,20,25]
val = int(input())
l, r = 0, 10
def f(x):
    return x*x

while r - l > 1:
    m = (l + r)//2
    if m <= val:
        l = m
    else:
        r = m - 1
print(l,f(l))