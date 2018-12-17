import math
class Uravnenie:
    def __init__(self, type):
        self.type = type
    def ur(self):
        if self.type == 'square':
            type = input()
            if type == 'full':

                a = float(input())
                b = float(input())
                c = float(input())

                D = b ** 2 - 4 * a * c
                fp = b ** 2
                sp = - 4 * a * c
                if D < 0:
                    print('disc =', D)
                    quit()

                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                if int(D / 2) == D / 2 and int(b / 2) == b / 2:
                    fp = (b / 2) ** 2
                    sp = -a * c
                    print('Discriminant 1  =', fp, '+', sp, '=', D / 4, '     ', math.sqrt(D / 4))
                else:
                    print('Discriminant = ', fp, '+', sp, '=', D, '    ', math.sqrt(D))

                if x1 == int(x1):
                    print('X 1 =', int(x1))
                else:
                    print('X 1 =', (-b + math.sqrt(D)), '/', 2 * a, '     =     ', x1)

                if x2 == int(x2):
                    print('X 2 =', int(x2))
                else:
                    print('X 2 =', (-b - math.sqrt(D)), '/', 2 * a, '     =     ', x2)
u = Uravnenie
u('square').ur()
