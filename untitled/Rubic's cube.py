l = []

for i in range(6):
    x = input()
    l.append([])
    # print(i)
    for j in range(3):
        y = input().split()
        g = [i for i in y]
        l[i].append(g)


print(l)