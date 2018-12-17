import tkinter
import random
import math

def prime(n):
    lis = []
    for i in range(1, n//2):
        if n%i == 0 and i*i <= n and not (i in lis and n//i in lis):
            lis.append(i)
            lis.append(n//i)
    if len(lis) > 2:
        return False
    else:
        return True

def factor(n):
    divs = []
    for i in range(1,n//2):
        if n%i == 0 and i*i < n:
            divs.append(i)
            divs.append(n//i)
    return sorted(list(set(divs)))

def upsearch(lis, n):
    l, r = 0, len(lis)
    while r - l > 1:
        m = (l + r) // 2
        if lis[m] <= n:
            l = m
        else:
            r = m
    return l

def lowsearch(lis, n):
    l, r = 0, len(lis)
    while l != r:
        m = (l+r)//2
        if lis[m] < n:
            l = m+1
        else:
            r = m
    return l

def graph(lis):
    master = tkinter.Tk()
    canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
    canvas.pack()
    points = []
    rand = [i for i in range(10,590)]

    for i in range(len(lis)):
        g = random.choice(rand)
        s = random.choice(rand)
        points.append((g,s))
        canvas.create_oval(((g)-5, (s)-5), ((g)+5, (s)+5), fill="black")
        canvas.create_text((g,s), text=i, fill="white")
    for i in lis:
        for j in i:
            canvas.create_line(points[lis.index(i)], points[j], fill="black")
            canvas.create_text(points[lis.index(i)], text=lis.index(i), fill="white")
    master.mainloop()

def sieve(n):
    tr = [True]*(n+1)
    ret = []
    for i in range(2,n+1):
        if i**2 <= n:
            for j in range(i**2,n+1,i):
                tr[j]=False
    for i in range(n+1):
        if tr[i]:
            ret.append(i)
    return ret
def continue_soon():
    pass
print(factor(24))
print(sieve(100))
print(fac)
graph([[1],[5],[0],[2],[3],[1,2, 6],[1], [8],[7]])