from PIL import Image, ImageDraw
import bibli
import math

size = 920, 920

# r = input()
# x = input()
# b = input()
# x_st = input()
# typ = input()
im = Image.new("RGBA", (920, 920), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)

koef = 46

for i in range(920 // koef + 1):
    draw.line((0, i * koef, 920, i * koef), fill="grey")

for i in range(920 // koef):
    draw.line((i * koef, 0, i * koef, 920), fill="grey")

draw.line((460, 0, 460, 920), fill='black')
draw.line((0, 460, 920, 460), fill='black')


def rx(r):
    y = 920 / koef
    x = y / r
    draw.line((460 - (x * 30), 460 + (y * 30), 460 + (x * 30), 460 - (y * 30)), fill='black')


# rx(5)

def rx_b(r, b):
    y = 920 / koef
    x = y / r
    draw.line((460 - (x * 30), (460 - b * koef) + (y * 30), 460 + (x * 30), (460 - b * koef) - (y * 30)), fill='black')


def squer_x(a, b, c):
    x = (-b) / (2 * a)
    y = a * (x ** 2) + b * x + c
    y *= koef
    x *= koef
    x = 460 + x
    y = 460 - y
    # print(x, y)
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
    y = 460 - y
    x = 0 - (bx / rx)
    x *= koef
    x += 460

    # print(x / 36, y // 36)

    if rx > 0:
        point = [i / 100 for i in range(0, 10001)]
    else:
        point = [-i / 100 for i in range(0, 10001)]
    # print(point)


    draw.line((x, y, x + (point[0] * koef), y - (int(math.sqrt(point[0] * rx)) * koef * r)), fill='black')
    lx, ly = (x + (point[0] * koef)), (y - (int(math.sqrt(point[0] * rx)) * koef * r))
    for i in range(1, len(point) - 1):
        nx, ny = (x + (point[i] * koef)), (y - int(math.sqrt(point[i] * rx) * koef * r))
        # print((lx-360)//36,(360-ly)//36,(nx-360)//36,(360-ny)//36)
        draw.line((lx, ly, nx, ny), fill='black')
        lx, ly = (x + (point[i] * koef)), (y - int(math.sqrt(point[i] * rx) * koef * r))




im.save("f(x).png", "PNG")
print('done')
