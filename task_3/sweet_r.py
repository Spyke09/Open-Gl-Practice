from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from primitives import *

# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Белый цвет для первоначальной закраски
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

    # mid
    glPushMatrix()
    glColor3f(1, 0, 0)
    glRotated(-45, 0, 1, 0)
    glScaled(0.3, 0.3, 0.6)
    cilinder()
    glPopMatrix()

    # blue
    glPushMatrix()
    glColor3f(0, 0, 1)
    glRotated(-45, 0, 1, 0)
    glTranslated(0, 0, -0.6)
    glScaled(0.6, 0.1, 0.6)
    conus()
    glPopMatrix()
     # green
    glPushMatrix()
    glColor3f(0, 1, 0)
    glRotated(135, 0, 1, 0)
    glTranslated(0, 0, -0.6)
    glScaled(0.6, 0.1, 0.6)
    conus()
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
