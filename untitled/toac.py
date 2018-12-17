import sys

x = input().split()
mass = []
vrem = []

for i in x:
    if len(i) >= 3:
        i = i.strip("':?/,.\\'!")
        vrem.append(i.lower())
print(vrem)