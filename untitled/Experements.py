# from math import sqrt
#
# a = float(input())
# b = float(input())
# c = float(input())
#
# D = b**2 - 4*a*c
# fp = b**2
# sp = - 4 * a* c
# if D < 0:
#     print(D)
#     quit()
#
# x1 = (-b + sqrt(D)) / (2*a)
# x2 = (-b - sqrt(D)) / (2*a)
# if int(D/2) == D/2 and int(b/2) == b/2:
#     fp = (b/2)**2
#     sp = -a * c
#     print('Discriminant 1  =', fp, '+', sp, '=', D/4,  '     ',sqrt(D/4))
# else: print('Discriminant = ', fp, '+', sp, '=', D, '    ',sqrt(D))
#
# if x1 == int(x1):
#     print('X 1 =', int(x1))
# else:
#     print('X 1 =', (-b + sqrt(D)), '/', 2*a,'     =     ', x1)
#
# if x2 == int(x2):
#     print('X 2 =', int(x2))
# else:
#     print('X 2 =', (-b - sqrt(D)), '/', 2 * a,'     =     ', x2)
words = 60
no = 0
yes = 0
cnt = 0
while words < 500:
    cnt += 1
    words += 80
    words -= 20


print(cnt)