import math
p = float(input())

for i in range(2,int(math.sqrt(p + 1))):
    while p % i == 0:
        print(i)
        print(p/i)
        p /= i

