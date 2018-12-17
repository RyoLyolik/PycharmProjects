x = input('Сколько весит файл(через пробел: размер, тип(Мб, Кб, байт и т.д))(32 Кб)')
y = input('Размер фото (через пробел. Пример: 1280 1920')
N = input('Сколько цветов содержит изображение')
i = input('Чему равно i')
if x == 'нет' or x == 'Нет':
    x = 'I'
else:
    x = x.split()
    if x[1] == 'Кб':
        x = float(x[0]) * 1024 * 8
    elif x[1] == 'Байт' or x[1] == 'байт':
        x = float(x[0]) * 8
    elif x[1] == 'Мб':
        x = float(x[0]) * 2**20 * 8
if y == 'нет' or x == 'Нет':
    y = 'K'
else:
    y = y.split()
    y = float(y[0]) * float(y[1])
if N == 'нет' or N == 'Нет':
    N = 'N'
else:
    N = float(N)
    z = 1
    while N != 2:
        z += 1
        N /= 2

if i == 'Нет' or i == 'нет':
    i = 'i'
else:
    i = float(i)
if x == 'I':
    x = float(y) * float(z)
    print('I =', x)
    inf = input('Во что надо перевести?')
    if inf == 'Мб':
        inf = x * 0.0000001192092870156381
        print('I =', inf)
if y == 'K':
    y = float(x) / float(z)
    print('K =', y)
if i == 'i':
    i = float(x) / float(y)
    print('i =', i)
if N == 'N':
    N = 2**i
    print('N =', N)