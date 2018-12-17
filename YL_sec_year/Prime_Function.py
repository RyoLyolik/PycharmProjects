from PIL import Image, ImageDraw
import math

size = 4000

im = Image.new("RGBA", (4000, 4000), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)

koef = 4000//40

for i in range(size // koef + 1):
    draw.line((0, i * koef, size, i * koef), fill="grey")

for i in range(size // koef):
    draw.line((i * koef, 0, i * koef, size), fill="grey")

draw.line((size//2, 0, size//2, size), fill='black')
draw.line((0, size//2, size, size//2), fill='black')


def rx(r):
    y = size/ koef
    x = y / r
    draw.line((size//2 - (x * 30), size//2 + (y * 30), size//2 + (x * 30), size//2 - (y * 30)), fill='black')


# rx(5)

def rx_b(r, b):
    y = size / koef
    x = y / r
    draw.line((size//2 - (x * 30), (size//2 - b * koef) + (y * 30), size//2 + (x * 30), (size//2 - b * koef) - (y * 30)), fill='black')


def squer_x(a, b, c):
    x = (-b) / (2 * a)
    y = a * (x ** 2) + b * x + c
    y *= koef
    x *= koef
    x = size//2 + x
    y = size//2 - y
    points = [i / 100 for i in range(0, 10001)]
    if a > 0:

        draw.line((x, y, x - points[0] * koef, y - points[0] ** 2 * koef * a), fill='black')
        draw.line((x, y, x + points[0] * koef, y - points[0] ** 2 * koef * a), fill='black')
        k = 1

        for i in range(len(points) - 1):
            draw.line((x - points[k] * koef, y - points[k] ** 2 * koef * a, x - points[i] * koef,
                       y - points[i] ** 2 * a * koef), fill='black')
            draw.line((x + points[k] * koef, y - points[k] ** 2 * koef * a, x + points[i] * koef,
                       y - points[i] ** 2 * koef * a), fill='black')
            k += 1

    elif a < 0:
        draw.line((x, y, x - points[0] * koef, y - points[0] ** 2 * koef * a), fill='black')
        draw.line((x, y, x + points[0] * koef, y - points[0] ** 2 * koef * a), fill='black')
        k = 1

        for i in range(len(points) - 1):
            draw.line((x - points[k] * koef, y - points[k] ** 2 * koef * a, x - points[i] * koef,
                       y - points[i] ** 2 * a * koef), fill='black')
            draw.line((x + points[k] * koef, y - points[k] ** 2 * koef * a, x + points[i] * koef,
                       y - points[i] ** 2 * koef * a), fill='black')
            k += 1


def sqrt(r, rx, b, bx):
    y = b * koef
    y = size//2 - y
    x = 0 - (bx / rx)
    x *= koef
    x += size//2


    if rx > 0:
        point = [i / 100 for i in range(0, 10001)]
    else:
        point = [-i / 100 for i in range(0, 10001)]

    draw.line((x, y, x + (point[0] * koef), y - (int(math.sqrt(point[0] * rx)) * koef * r)), fill='black')
    lx, ly = (x + (point[0] * koef)), (y - (int(math.sqrt(point[0] * rx)) * koef * r))
    for i in range(1, len(point) - 1):
        nx, ny = (x + (point[i] * koef)), (y - int(math.sqrt(point[i] * rx) * koef * r))
        draw.line((lx, ly, nx, ny), fill='black')
        lx, ly = (x + (point[i] * koef)), (y - int(math.sqrt(point[i] * rx) * koef * r))

def prime(n):
    lis = []
    for i in range(1, int(math.sqrt(n+1 // 2)) + 1):
        if n % i == 0 and i * i <= n + 1 and not (i in lis and n // i in lis):
            lis.append(i)
            lis.append(n // i)

    if len(lis) > 2 or n == 1:
        return False
    else:
        return True


def prime_func():
    y = size//2
    x = size//2
    cnt = 0
    draw.line((x,y, x+1,y+1), fill='black')
    lx = x+1
    ly = y+1
    for i in range(1,x):
        # print(x)
        if prime(i) and i != 1:
            print(i)
            cnt+=1
            draw.line((lx,ly, size/2+i,size/2-cnt), fill='black')
            lx = size/2+i
            ly = size/2-cnt
rx(1)
rx_b(3,2) #  y = 3x + 2
squer_x(2,1,3) # y = 2(x^2) + x + 3
sqrt(2,-2,-4,5) #  y = 2*sqrt(-2x+5)-4
prime_func()

im.save("f(x).png", "PNG")
print('done')
