lis = [int(i) for i in input().split()]

value = int(input())

l, r = 0, len(lis)-1

cnt= 0
while l<r:
    m = (l+r)//2
    # print(l, r, m)
    if lis[m] < value:
        l=m+1
    else:
        r=m
    cnt+=1
print(cnt)
print(l)