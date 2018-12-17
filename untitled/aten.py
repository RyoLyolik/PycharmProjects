import random

x = 'ЙЦУКЕНГШЩЗФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
x1 = [[],[],[]]
x2= [[],[],[]]
lis = [i for i in x]
k = 0
# print(len(lis))
while len(lis) > 0:
    k+=1
    l = random.choice(lis)
    if k > 10 and k <= 20:
        x1[1].append(l)
        x2[1].append(random.choice('ЛПВ'))
    elif k <= 10:
        x1[0].append(l)
        x2[0].append(random.choice('ЛПВ'))
    else:
        x1[2].append(l)
        x2[2].append(random.choice('ЛПВ'))
    lis.remove(l)

for i in range(3):
    for j in range(10):
        print(x1[i][j], end='   ')
    print()
    for j in range(10):
        print(x2[i][j], end='   ')
    print()
    print()