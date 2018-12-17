a = input().split()
w = int(a[0])
h = int(a[1])
n = int(a[2])

def f(m):
    global h, w
    return (m//h) * (m//w) >= n

l, r = 0, n * max(h, w)

while r != l: # lower bound
    mid = (l+r) // 2
    if not f(mid):
        l = mid + 1
    else:
        r = mid
print(l)

#Когда Петя учился в школе, он часто участвовал в олимпиадах по информатике, математике и физике.
# Так как он был достаточно способным мальчиком и усердно учился, то на многих из этих олимпиад он получал дипломы.
# К окончанию школы у него накопилось n дипломов, причём, как оказалось, все они имели одинаковые размеры: w — в ширину и h — в высоту.
# Сейчас Петя учится в одном из лучших российских университетов и живёт в общежитии со своими одногруппниками.
#  Он решил украсить свою комнату, повесив на одну из стен свои дипломы за школьные олимпиады.
#  Так как к бетонной стене прикрепить дипломы достаточно трудно,
# то он решил купить специальную доску из пробкового дерева, чтобы прикрепить её к стене, а к ней — дипломы.
#  Для того чтобы эта конструкция выглядела более красиво,
#  Петя хочет, чтобы доска была квадратной и занимала как можно меньше места на стене.
#  Каждый диплом должен быть размещён строго в прямоугольнике размером w на h.
# Дипломы запрещается поворачивать на 90 градусов.
# Прямоугольники, соответствующие различным дипломам, не должны иметь общих внутренних точек.
# Требуется написать программу, которая вычислит
#  минимальный размер стороны доски, которая потребуется
# Пете для размещения всех своих дипломов.

# Входные данные
# Входной файл содержит три целых числа: w, h, n (1whn109).
#
# Выходные данные
# В выходной файл необходимо вывести ответ на поставленную задачу.
#