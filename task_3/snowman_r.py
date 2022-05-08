from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from primitives import *

# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0.5, 0, 1.0)  # Зеленый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Определяем границы рисования по горизонтали и вертикали
    global anglex, angley, anglez, filled
    anglex = 0
    angley = 0
    anglez = 0
    filled = 0


# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
    global anglex, angley, anglez, filled
    if key == b'\x1b':
        sys.exit(0)
    if key == b'w':
        anglex += 5
    if key == b's':
        anglex -= 5
    if key == b'q':
        angley += 5
    if key == b'e':
        angley -= 5
    if key == b'a':
        anglez += 5
    if key == b'd':
        anglez -= 5
    if key == b' ':
        filled = 1 - filled
    glutPostRedisplay()  # Вызываем процедуру перерисовки


# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очищаем экран и заливаем текущим цветом фона
    glLoadIdentity()
    global anglex, angley, anglez, filled
    glRotated(anglex, 1, 0, 0)
    glRotated(angley, 0, 1, 0)
    glRotated(anglez, 0, 0, 1)
    glRotated(-105, 1, 0, 0)
    if filled == 1:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # body w/ scarf
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslated(0, 0, 0.8)
    glScaled(0.27, 0.2, 0.3)
    cilinder()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslated(0, 0, 0.45)
    glScaled(0.3, 0.3, 0.3)
    sphere()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslated(0, 0, -0.35)
    glScaled(0.5, 0.5, 0.5)
    sphere()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 0.5, 0)
    glTranslated(0, 0, 0.15)
    glScaled(0.3, 0.3, 0.3)
    thor()
    glPopMatrix()

    # nose
    glPushMatrix()
    glColor3f(1, 0.5, 0)
    glTranslated(0, 0.125, 0.4)
    glScaled(0.2, 0.25, 0.15)
    glRotated(-90, 1, 0, 0)
    glTranslated(0, 0, 1)
    conus()
    glPopMatrix()

    # mouth
    glPushMatrix()
    glColor3f(0.75, 0, 0)
    glTranslated(-0, 0.2, 0.3)
    glScaled(0.15, 0.15, 0.15)
    glRotated(0, -1, -1, 0)
    thor()
    glPopMatrix()

    # eyes
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslated(0.067, 0.25, 0.6)
    glScaled(0.03, 0.03, 0.03)
    sphere()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslated(-0.067, 0.25, 0.6)
    glScaled(0.03, 0.03, 0.03)
    sphere()
    glPopMatrix()

    # hands
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslated(0.4, 0.1, 0.07)
    glRotated(45, 0, 1, 0)
    glScaled(0.12, 0.12, 0.12)
    sphere()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslated(-0.4, 0.1, 0.07)
    glRotated(-45, 0, 1, 0)
    glScaled(0.12, 0.12, 0.12)
    sphere()
    glPopMatrix()

    glutSwapBuffers()  # Меняем буферы
    glutPostRedisplay()  # Вызываем процедуру перерисовки


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Second Program!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()