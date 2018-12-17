n, m = [int(i) for i in input().split()]

gr = [[int(i) for i in input().split()] for i in range(n)]

used = [False]*n
num = 0

def dfs(v):
    global used, num
    num += 1
    used[v] = True
    for i in gr[v]:
        if not used[i]:
            dfs(i)

dfs(m)
print(num)