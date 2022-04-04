import math
import random

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Процедура инициализации
def init():
    glClearColor(0.5, 0.5, 0.5, 1.0)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Определяем границы рисования по горизонтали и вертикали
    glEnable(GL_DEPTH_TEST)


# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очищаем экран и заливаем текущим цветом фона
    glRotated(1.2, 1, 1, 1)
    R = 0.5
    n = 40
    h = 0.5
    h1 = (2*R)/n
    h2 = -R
    r = 0

    for j in range(n//2):
        glBegin(GL_QUAD_STRIP)
        if r*r-h1*h1-2*h1*h2>=0:
            rn = math.sqrt(r*r-h1*h1-2*h1*h2)
        else:
            rn = 0
        for i in range(n+1):
            glColor3f(1-i%2, 1-i%2, i%2)
            glVertex3d(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n), h2)
            glVertex3d(rn * math.cos(2 * math.pi * i / n), rn * math.sin(2 * math.pi * i / n), h2+h1)
        h2 += h1
        r = rn
        glEnd()

    R = 0.4
    n = 40
    h = 0.5
    h1 = (2 * R) / n
    h2 = -R
    r = 0

    for j in range(n // 2):
        glBegin(GL_QUAD_STRIP)
        if r * r - h1 * h1 - 2 * h1 * h2 >= 0:
            rn = math.sqrt(r * r - h1 * h1 - 2 * h1 * h2)
        else:
            rn = 0
        for i in range(n + 1):
            glColor3f(1 - i % 2, 1 - i % 2, i % 2)
            glVertex3d(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n), h2)
            glVertex3d(rn * math.cos(2 * math.pi * i / n), rn * math.sin(2 * math.pi * i / n), h2 + h1)
        h2 += h1
        r = rn
        glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(n+1):
        glColor3f(1 - i % 2, 1 - i % 2, i % 2)
        glVertex3d(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n), 0)
        glVertex3d(0.5 * math.cos(2 * math.pi * i / n), 0.5 * math.sin(2 * math.pi * i / n), 0)
    glEnd()

    # glBegin(GL_TRIANGLE_FAN)
    # glVertex3d(0, 0, 0)
    # for i in range(n+1):
    #     glColor3f(1-i%2, 1-i%2, i%2)
    #     glVertex3d(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n), 0)
    # glEnd()

    glutSwapBuffers()  # Меняем буферы
    glutPostRedisplay()  # Вызываем процедуру перерисовки


def change_size(w, h):
    glMatrixMode(GL_PROJECTION)
    glMatrixMode(GL_MODELVIEW)


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL First Program!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
glutReshapeFunc(change_size)
# Вызываем нашу функцию инициализации
init()
# Запускаем "главный цикл GLUT"
glutMainLoop()