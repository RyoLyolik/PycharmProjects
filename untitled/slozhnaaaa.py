x = int(input())
y = int(input())
i = 0
def C(x,y):
    global i
    print(i)
    if x == 0 or x == y:
        return i
    else:
        i = C(x-1,y-1)+C(x,y-1)
        print()
        return C(x-1,y-1)+C(x,y-1)

print(C(x, y), "loh")