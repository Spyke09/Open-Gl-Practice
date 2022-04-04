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
    R = 0.5
    n = 40
    h = 0.5
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очищаем экран и заливаем текущим цветом фона
    glRotated(1.2, 1, 1, 1)

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, -h)
    for i in range(n//2+1):
        glColor3f(1-i%2, 1-i%2, i % 2)
        glVertex3d(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n), -h)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3d(0, 0, h)
    for i in range(n//2+1):
        glColor3f(1-i%2, 1-i%2, i%2)
        glVertex3d(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n), h)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(n//2+1):
        glColor3f(1-i%2, 1-i%2, i%2)
        glVertex3d(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n), -h)
        glVertex3d(R * math.cos(2 * math.pi * i / n), R * math.sin(2 * math.pi * i / n), h)
    glVertex3d(R * math.cos(2 * math.pi * 0 / n), R * math.sin(2 * math.pi * 0 / n), -h)
    glVertex3d(R * math.cos(2 * math.pi * 0 / n), R * math.sin(2 * math.pi * 0 / n), h)

    glEnd()

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