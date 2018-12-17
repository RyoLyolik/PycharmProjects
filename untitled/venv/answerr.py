import random

d = []
for i in range(10000):
    k = [i for i in range(10)]
    x = []

    for i in range(5000):
        x.append(str(random.choice(k)))
    # print(x)
    if x[0] == "0":
        x = x[1:]
    x = ''.join(x)
    # print(x)

    num = "0"
    l = []
    k = 0
    for j in range(10):
        for i in x:
            if i == num:
                k+= 1

        # print(k, num)
        l.append((k,num))
        k = 0
        num = str(int(num)+1)

    # print(l)

    n = 1
    while n < len(l):
         for i in range(len(l)-n):
              if l[i][0] > l[i+1][0]:
                   l[i],l[i+1] = l[i+1],l[i]
         n += 1

    # l = reversed(l)
    # print(l[-1])
    d.append(l[-1][1])


k = 0
num = 0
for j in range(10):
    for i in x:
        if i == num:
            k+= 1

    # print(k, num)
    l.append((k,num))
    k = 0
    num = str(int(num)+1)
# print(l)
# print(''.join(d))
n = 1
while n < len(l):
    for i in range(len(l) - n):
        if l[i][0] > l[i + 1][0]:
            l[i], l[i + 1] = l[i + 1], l[i]
    n += 1
print(l)
print(l[0])
