# import pymorphy2

x = "привет папа мама пока что нет да"
x = [["привет", 0], ["папа",0],["мама",0],["пока",0],["что",0],["да",0]]
y = input()
for i in y:
    for j in x:
        if len(y) == len(j[0]):
            j[1]+= 1
        if y == j[0]:
            print(j[0])
            exit(0)
        for o in j[0]:
            if o == i:
                j[1]+=1


n = 1
while n < len(x):
     for i in range(len(x)-n):
          if x[i][1] > x[i+1][1]:
               x[i],x[i+1] = x[i+1],x[i]
     n += 1

print(x[-1][0])
# morph = pymorphy2.MorphAnalyzer()
# morph.parse('Ваня')