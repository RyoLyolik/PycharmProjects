from PIL import Image, ImageDraw
from PIL import ImageFont
import random

image = Image.new("RGBA", (320,320), (0,0,0,0))
draw = ImageDraw.Draw(image)


draw.line((0, 0,10,10), fill='red')
font = ImageFont.truetype("arial.ttf", 150)

def graph(lis):
    image = Image.new("RGBA", (920,920),(0,0,0,0))
    canvas = ImageDraw.Draw(image)
    points = []
    rand = [i for i in range(10,910)]

    for i in range(len(lis)):
        g = random.choice(rand)
        s = random.choice(rand)
        points.append((g,s))
        # canvas.ellipse(((g)-5, (s)-5), ((g)+5, (s)+5), fill="black")
        # print((g)-5,(s)-5, (g)+5, (s)+5)
        canvas.ellipse(((g)-6,(s)-6, (g)+6, (s)+6), fill="black", outline="black")
        canvas.text((g-4,s-6), text=str(i), fill="white")

    for i in range(len(lis)):
        for j in range(len(lis[i])):
            # print(points[i][0],points[i][1], points[lis[i][j]][0],points[lis[i][j]][1])
            canvas.line((points[i][0], points[i][1], points[lis[i][j]][0], points[lis[i][j]][1]), fill="black", width=2)
            canvas.text((points[i][0]-4, points[i][1]-6), text=str(i), fill="white")

    for i in range(len(lis)):
        for j in range(len(lis[i])):
            # print(points[i][0],points[i][1], points[lis[i][j]][0],points[lis[i][j]][1])
            # canvas.line((points[i][0], points[i][1], points[lis[i][j]][0], points[lis[i][j]][1]), fill="black", width=2)
            canvas.text((points[i][0]-4, points[i][1]-6), text=str(i), fill="white")

    image.save("test.png", "PNG")

graph([[1],[0]])