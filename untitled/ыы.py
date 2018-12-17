
import sys
x = input().strip('QWERTYUIOP{}":LKJHGFDSAZXCVBNM<>?qwertyuiop[]";lkjhgfdsazxcvbnm,./()*&^%$#@!-=+_йцукенгшщзхъэждлорпавыфячсмитьбю.ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ,/\|')
x = x.strip("'")
x = x.strip('QWERTYUIOP{}":LKJHGFDSAZXCVBNM<>?qwertyuiop[]";lkjhgfdsazxcvbnm,./()*&^%$#@!-=+_йцукенгшщзхъэждлорпавыфячсмитьбю.ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ,/\|')
x = x.strip("'")
print(x)
x = float(x)
l = str(x).split('.')
if float(l[0]) > 10:
    y = x/(10**len(str(int(l[0]))) / 10)
    syblim = len(str(int(l[0]))) - 1
    print(str(y) + ' * ' + '10^' + str(syblim))
elif float(l[0]) < -10:
    y = x / (10 ** len(str(int(l[0]))) /100)
    syblim = len(str(int(l[0]))) - 2
    print(str(y) + ' * ' + '10^' + str(syblim))
if x < 1 and x > -1:
    coun = 0
    while x < 1 and x > -1:
        x *= 10
        coun += 1
    print(str(x) + ' * ' + '10^-' + str(coun))
    print(str(round(x, 2)) + ' * ' + '10^-' + str(coun), "rounded")
elif x >= 1 and x < 10:
    print(x)

