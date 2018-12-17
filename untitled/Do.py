import random
from PyFi import just
from math import sqrt
import sys
lis = [i for i in range(100)]
plus = 0
minus = 0
all = 0
falselist = []
for i in range(len(lis)):
    lis[i] = [lis[i], lis[i] **2]
while all != 100:
    h = random.choice(lis)
    k = random.choice(h)
    if k <= 10:
        continue
    elif k > 100:
        if just(int(sqrt(k))) and (int(sqrt(k)) > 30):
            print(k)
            if int(str((input())).strip("./\|qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}\":LKJHGFDSAZXCVBNM<>?!@#$%^&*()_+=-?")) == sqrt(k):
                print(True, "("+str(all)+")")
                print()
                plus += 1
            else:
                print(False, sqrt(k), "("+str(all)+")")
                print()
                falselist.append('√' + str(k) + ' = ' + str(sqrt(k)))
            all += 1
        elif int(sqrt(k)) < 30 and (int(sqrt(k)) > 10):
            print(k)
            if int(str((input())).strip("./\|qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}\":LKJHGFDSAZXCVBNM<>?!@#$%^&*()_+=-?")) == sqrt(k):
                print(True, "(" + str(all) + ")")
                print()
                plus += 1
            else:
                print(False, sqrt(k), "(" + str(all) + ")")
                print()
                falselist.append('√' + str(k) + ' = ' + str(sqrt(k)))
            all += 1
    elif k < 100:
        if k > 30 and just(k) == True:
            print(k)
            if int(str((input())).strip("./\|qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}\":LKJHGFDSAZXCVBNM<>??!@#$%^&*()_+=-")) == k **2:
                print(True, "("+str(all)+")")
                print()
                plus += 1
            else:
                print(False, k**2, "("+str(all)+")")
                print()
                falselist.append(str(k) + '**2' + ' = ' + str(k**2))
            all += 1
        elif k <= 30 and k > 10:
            print(k)
            if int(str((input())).strip("./\|qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}\":LKJHGFDSAZXCVBNM<>?!@#$%^&*()_+=-")) == k ** 2:
                print(True, "(" + str(all) + ")")
                print()
                plus += 1
            else:
                print(False, k ** 2, "(" + str(all) + ")")
                print()
                falselist.append(str(k) + '**2' + ' = ' + str(k ** 2))
            all += 1

print("Your result is", str((plus/all * 100)) + "%,", int((plus/all * 100)/20))
print("true:", plus)
print("false:", all - plus)
for i in falselist:
    print(i)