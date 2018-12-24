import random

def make_list():
    l= []
    for i in range(1000):
        l.append(random.choice(range(2)))

    return l

find_middle = []
for i in range(100):
    cnt = 0
    li = make_list()
    for j in li:
        if j == 0:
            cnt +=1

    find_middle.append(cnt/1000)

print(sum(find_middle)/100)
