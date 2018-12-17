d = int(input())
l = [int(i) for i in input().split()]
l = set(l)
l = list(l)
l = sorted(l)
print(l[-2])