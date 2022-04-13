import math

from PIL import Image, ImageDraw

image = Image.open("Lego.jpg")
draw = ImageDraw.Draw(image)

w = image.size[0]
h = image.size[1]
pix = image.load()

def distribution(l, x, b):
    if b:
        for i in range(len(l)):
            if l[i]>=x:
                return i
    else:
        for i in range(len(l)-1, 0, -1):
            if l[i]>=x:
                return i
    return -1

def f(q):
    return (q[0]-q[1])*255//(q[2]-q[1])

par = 7/100
a = [0, 0, 0]
b = [255, 255, 255]

l = [[0 for i in range(256)],[0 for i in range(256)],[0 for i in range(256)]]

for x in range(w):
    for y in range(h):
        l[0][pix[x, y][0]] += 1
        l[1][pix[x, y][1]] += 1
        l[2][pix[x, y][2]] += 1

for i in range(3):
    temp = max(l[i])-min(l[i])
    a[i] = distribution(l[i], temp * par, 1)
    b[i] = distribution(l[i], temp * par, 0)

for x in range(w):
    for y in range(h):
        temp = tuple(map(f, zip(pix[x, y], a, b)))
        draw.point((x, y), temp)

image.show()
del draw
