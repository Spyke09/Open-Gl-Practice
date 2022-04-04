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

    glBegin(GL_QUADS)

    glColor3f(1, 0, 0)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)

    glColor3f(1, 1, 0)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)

    glColor3f(0, 1, 0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    glColor3f(0, 1, 1)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    glColor3f(0, 0, 1)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    glColor3f(1, 0, 1)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    glEnd()

    glutSwapBuffers()  # Меняем буферы
    glutPostRedisplay()  # Вызываем процедуру перерисовки


def change_size(w, h):
    glMatrixMode(GL_PROJECTION)
    glMatrixMode(GL_MODELVIEW)


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL First Program!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
glutReshapeFunc(change_size)
# Вызываем нашу функцию инициализации
init()
# Запускаем "главный цикл GLUT"
glutMainLoop()