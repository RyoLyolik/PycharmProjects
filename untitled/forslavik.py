import random
ran = range(1,11)
def end(ans):
    pers = len(truee)/len(all)*100
    # x = pers // 20
    if pers < 25:
        x = 1
    elif pers >= 25 and pers < 50:
        x = 2
    elif  50 <= pers < 65:
        x = 3
    elif 65 <= pers < 80:
        x = 4
    else:
        x = 5
    # if x < 4:
    #     x+= 1
    print()
    print(str(pers)+"%", " ", 'оценка:',x)
    print("Правильно:", str(len(truee)))
    print("Неправильно:", str(len(all) - len(truee)))
    quit(0)


def statistic(f,s,ans):
    pers = len(truee)/len(all)*100
    # x = pers // 20
    if pers < 25:
        x = 1
    elif pers >= 25 and pers < 50:
        x = 2
    elif  50 <= pers < 65:
        x = 3
    elif 65 <= pers < 80:
        x = 4
    else:
        x = 5
    # if x < 4:
    #     x+= 1
    print()
    print(str(pers)+"%", " ", 'оценка:',x)
    print("Правильно:", str(len(truee)))
    print("Неправильно:", str(len(all) - len(truee)))
    print()
    print(f, "*", s)
    an = input()
    return check(f, s, an)


def smthisal(x):
    d = True
    b = True
    x = str(x)
    for i in x:
        if not i.isdigit():
            b = False
            break
    if not b:
        return True
    else:
        return False


def check(x,y,i):
    if smthisal(i) and i != 'стат' and i != 'стоп' or i == '':
        print('Ошибка ввода.')
        print(x, "*", y)
        h = input()
        return check(x,y,h)


    else:
        if i.lower() == 'стат':
            checkstat(x,y,i)
        elif i.lower() == 'стоп':
            checkstop(x, y, i)
        elif x*y == int(i):
            print("Да")
            all.append("smth")
            truee.append("Yes")
        else:
            print("Нет", x*y)
            all.append("smth")


def checkstat(f,s, ans):
    global all
    if ans.lower()=='стат':
        if len(all) == 0:
            print("Ошибка: нет результатов. Решите хотябы один пример.")
            print(f, "*", s)
            an = input()
            return checkstat(f, s, an)
        else:
            return statistic(f,s, ans)
    else:
        return check(f, s, ans)


def checkstop(f,s,ans):
    global all
    if ans.lower()=='стоп':
        if len(all) == 0:
            print("Ошибка: нет результатов. Решите хотябы один пример.")
            print(f, "*", s)
            an = input()
            return checkstop(f, s, an)
        else:
            return end(ans)
    else:
        return check(f, s, ans)

truee = []
all = []
def mult():
    for i in range(1, 100):
        f = random.choice(ran)
        s = random.choice(ran)
        print(f,"*",s)
        ans = input()
        d = True
        b = True
        check(f,s,ans)



def end1(ans):
    pers = len(truee) / len(all) * 100
    # x = pers // 20
    if pers < 25:
        x = 1
    elif pers >= 25 and pers < 50:
        x = 2
    elif 50 <= pers < 65:
        x = 3
    elif 65 <= pers < 80:
        x = 4
    else:
        x = 5
    # if x < 4:
    #     x+= 1
    print()
    print(str(pers) + "%", " ", 'оценка:',x)
    print("Правильно:", str(len(truee)))
    print("Неправильно:", str(len(all) - len(truee)))
    quit(0)

def statistic1(f, s, ans):
    pers = len(truee) / len(all) * 100
    # x = pers // 20
    if pers < 25:
        x = 1
    elif pers >= 25 and pers < 50:
        x = 2
    elif 50 <= pers < 65:
        x = 3
    elif 65 <= pers < 80:
        x = 4
    else:
        x = 5
    # if x < 4:
    #     x+= 1
    print()
    print(str(pers) + "%", " ", 'оценка:',x)
    print("Правильно:", str(len(truee)))
    print("Неправильно:", str(len(all) - len(truee)))
    print()
    print(f, "+", s)
    an = input()
    return check1(f, s, an)

def smthisal1(x):
    d = True
    b = True
    x = str(x)
    for i in x:
        if not i.isdigit():
            b = False
            break
    if not b:
        return True
    else:
        return False

def check1(x, y, i):
    if smthisal1(i) and i != 'стат' and i != 'стоп' or i == '':
        print('Ошибка ввода.')
        print(x, "+", y)
        h = input()
        return check1(x, y, h)


    else:
        if i.lower() == 'стат':
            checkstat1(x, y, i)
        elif i.lower() == 'стоп':
            checkstop1(x, y, i)
        elif x + y == int(i):
            print("Да")
            all.append("smth")
            truee.append("Yes")
        else:
            print("Нет", x + y)
            all.append("smth")

def checkstat1(f, s, ans):
    global all
    if ans.lower() == 'стат':
        if len(all) == 0:
            print("Ошибка: нет результатов. Решите хотябы один пример.")
            print(f, "+", s)
            an = input()
            return checkstat1(f, s, an)
        else:
            return statistic1(f, s, ans)
    else:
        return check1(f, s, ans)

def checkstop1(f, s, ans):
    global all
    if ans.lower() == 'стоп':
        if len(all) == 0:
            print("Ошибка: нет результатов. Решите хотябы один пример.")
            print(f, "+", s)
            an = input()
            return checkstop1(f, s, an)
        else:
            return end1(ans)
    else:
        return check1(f, s, ans)

def summing():
    truee = []
    all = []
    for i in range(1, 100):
        f = random.choice(ran)
        s = random.choice(ran)
        print(f, "+", s)
        ans = input()
        d = True
        b = True
        check1(f, s, ans)


def choice():
    x12 = input('Сложение(с) или умножение(у)?')
    if x12.lower() == 'с' or x12.lower() == 'c':
        summing()
    elif x12.lower()=='у' or x12.lower()=='y':
        mult()
    else:
        print("Ошибка ввода.")
        choice()
choice()
