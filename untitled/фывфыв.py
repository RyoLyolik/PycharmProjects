a = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l, r = 0, 10 # полуинтервалы
val = int(input())
while r - l > 1: # upper bound
    m = (l+r) // 2
    if a[m] <= val:
       l = m
    else:
        r = m
print(l, "upper bound")

l, r = 0, 10

while r != l: # lower bound
    m = (l+r) // 2
    if a[m] < val:
        l = m+1
    else:
        r = m
print(l, "lower bound")