# Для выполнения практической работы номер 2 используйте ЭТОТ файл
import random
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки

image = Image.open("../../Open-Gl-Practice/brezenchem/bear.JPG")  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей


def sign(x):  # знак числа
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def _line_gen(x1, x2, y1, y2, flag):
    dX = abs(x2 - x1)
    dY = abs(y2 - y1)
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    flag = (x1 < x2 and flag) or (y1 < y2 and not (flag))
    err = 0  # накапливаемая "ошибка"
    dErr = dY
    y = y1 if flag else y2
    dirY = sign(y2 - y1) if flag else -sign(y2 - y1)
    for x in range(x1, x2 + 1) if flag else reversed(range(x1, x2 + 1)):
        yield x, y
        err += dErr
        if err + err >= dX:
            y += dirY
            err -= dX


def line_gen(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    if abs(p2[0] - p1[0]) >= abs(p2[1] - p1[1]):  # если наклон по X больше Y, то X меняем на 1 и смотрим Y
        for i, j in _line_gen(x1, x2, y1, y2, True):
            yield i, j
    else:  # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
        for i, j in _line_gen(y1, y2, x1, x2, False):
            yield j, i


def lineP(p1, p2, color):  # рисуем линию из точки p1(x1,y1) в точку p2(x2,y2)
    c = 0
    for i, j in line_gen(p1, p2):
        # draw.point((i, j), color)
        draw.point((i, j), (c, c, c))
        c += 3


def triangle_gen(g1, g2, x0, y0, flag):
    for x, y in g1:
        while x0 < x:
            x0, y0 = next(g2)
        if x == x0:
            for i in range(y, y0 + 1) if flag else range(y, y0 + 1, -1):
                yield x, i


def triangle(p1, p2, p3, color):  # Рисуем треугольник по трем точкам - p1, p2, p3
    p1, p2, p3 = sorted((p1, p2, p3), key=(lambda x: x[0]))
    g1 = line_gen(p1, p2)
    g2 = line_gen(p2, p3)
    g3 = line_gen(p1, p3)
    if p1[1] > p2[1]:
        x0, y0 = next(g3)
        for i in triangle_gen(g1, g3, x0, y0, True):
            draw.point(i, color)
        next(g2)
        for i in triangle_gen(g2, g3, x0, y0, True):
            draw.point(i, color)
    else:
        x0, y0 = next(g3)
        for i in triangle_gen(g1, g3, x0, y0, False):
            draw.point(i, color)
        next(g2)
        for i in triangle_gen(g2, g3, x0, y0, False):
            draw.point(i, color)


# В следующих строках задаются цвета треугольников и точки, по которым они строятся
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 0, 200)
t1 = (0, height // 4)
t2 = (width // 2, 0)
t3 = (width // 4, height // 2)
t4 = (width - 1, height // 2)
t5 = (width // 2, height // 4)
t6 = (width * 3 // 4, 0)
t7 = (0, height // 2)
t8 = (width // 4, height - 1)
t9 = (width // 2, height * 3 // 4)
t10 = (width - 1, height * 3 // 4)
t11 = (width * 3 // 4, height // 2)
t12 = (width // 2, height - 1)
# Ниже вызываем заливку 4-х треугольников для проверки работы программы
triangle(t1, t2, t3, green)
triangle(t4, t5, t6, red)
triangle(t7, t8, t9, blue)
triangle(t10, t11, t12, black)

image.show()
# image.save("result.jpg")
del draw
