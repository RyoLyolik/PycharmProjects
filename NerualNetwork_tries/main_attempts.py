# video https://youtu.be/cKxRvEZd3Mw?list=LLbLKOy-UA14A0lQwq99jadQ

from sklearn import tree
from PIL import Image

labels = []
pixels_apple = [[], [], [], [], [], [], [], []]
print('loading training_data...')
for num in range(8):
    im = Image.open('training_data/apple_' + str(num) + '.jpg')
    pixs = im.load()
    size = x, y = im.size
    labels.append('apple')
    for i in range(x):
        for j in range(y):
            pixels_apple[num].append(pixs[i, j][0])
            pixels_apple[num].append(pixs[i, j][1])
            pixels_apple[num].append(pixs[i, j][2])

pixels_orange = [[], [], [], [], [], []]
for num in range(6):
    im = Image.open('training_data/orange_' + str(num) + '.jpg')
    pixs = im.load()
    size = x, y = im.size
    labels.append('orange')
    for i in range(x):
        for j in range(y):
            pixels_orange[num].append(pixs[i, j][0])
            pixels_orange[num].append(pixs[i, j][1])
            pixels_orange[num].append(pixs[i, j][2])

features = []
# add to features pixels
for i in pixels_apple:
    features.append(i)

for i in pixels_orange:
    features.append(i)


clf = tree.DecisionTreeClassifier()
print('training...')
clf = clf.fit(features, labels)

print('loading input_image...')
im = Image.open('input_image/input_image.jpg')
size = x, y = im.size
pixs = im.load()
inp_pix = []
for i in range(x):
    for j in range(y):
        inp_pix.append(pixs[i, j][0])
        inp_pix.append(pixs[i, j][1])
        inp_pix.append(pixs[i, j][2])

print(*clf.predict([inp_pix]))
