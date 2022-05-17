from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def cilinder():
    R = 0.5

    glBegin(GL_TRIANGLE_FAN)

    glVertex3d(0, 0, -0.5)
    for i in range(21):
        glVertex3d(R * cos(2 * pi * i / 20), \
                   R * sin(2 * pi * i / 20), -0.5)

    glEnd()

    glBegin(GL_QUAD_STRIP)

    for i in range(21):
        glVertex3d(R * cos(2 * pi * i / 20), \
                   R * sin(2 * pi * i / 20), -0.5)
        glVertex3d(R * cos(2 * pi * i / 20), \
                   R * sin(2 * pi * i / 20), 0.5)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glVertex3d(0, 0, 0.5)
    for i in range(21):
        glVertex3d(R * cos(2 * pi * i / 20), \
                   R * sin(2 * pi * i / 20), 0.5)

    glEnd()


def conus():
    R = 0.5
    glBegin(GL_TRIANGLE_FAN)

    glVertex3d(0, 0, -0.5)
    for i in range(21):
        glVertex3d(R * cos(2 * pi * i / 20), \
                   R * sin(2 * pi * i / 20), -0.5)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glVertex3d(0, 0, 0.5)
    for i in range(21):
        glVertex3d(R * cos(2 * pi * i / 20), \
                   R * sin(2 * pi * i / 20), -0.5)

    glEnd()


def sphere():
    R = 1
    for j in range(-9, 9):
        glBegin(GL_QUAD_STRIP)

        for i in range(21):
            glVertex3d(R * cos(pi * j / 18) * cos(2 * pi * i / 20), \
                       R * cos(pi * j / 18) * sin(2 * pi * i / 20), \
                       R * sin(pi * j / 18))
            glVertex3d(R * cos(pi * (j + 1) / 18) * cos(2 * pi * i / 20), \
                       R * cos(pi * (j + 1) / 18) * sin(2 * pi * i / 20), \
                       R * sin(pi * (j + 1) / 18))

        glEnd()


def thor():
    R = 0.5
    R2 = R * 0.3

    for i in range(20):
        glBegin(GL_QUAD_STRIP)

        for j in range(21):
            glVertex3d((R + R2 * cos(2 * pi * j / 20)) * cos(2 * pi * i / 20), \
                       (R + R2 * cos(2 * pi * j / 20)) * sin(2 * pi * i / 20), \
                       R2 * sin(2 * pi * j / 20))
            glVertex3d((R + R2 * cos(2 * pi * j / 20)) * cos(2 * pi * (i + 1) / 20), \
                       (R + R2 * cos(2 * pi * j / 20)) * sin(2 * pi * (i + 1) / 20), \
                       R2 * sin(2 * pi * j / 20))

        glEnd()


def cube(d):
    glBegin(GL_QUADS)

    glVertex3d(d, d, d)
    glVertex3d(-d, d, d)
    glVertex3d(-d, -d, d)
    glVertex3d(d, -d, d)

    glVertex3d(d, d, -d)
    glVertex3d(-d, d, -d)
    glVertex3d(-d, -d, -d)
    glVertex3d(d, -d, -d)

    glVertex3d(d, d, d)
    glVertex3d(d, d, -d)
    glVertex3d(d, -d, -d)
    glVertex3d(d, -d, d)

    glVertex3d(-d, d, d)
    glVertex3d(-d, d, -d)
    glVertex3d(-d, -d, -d)
    glVertex3d(-d, -d, d)

    glVertex3d(d, d, d)
    glVertex3d(d, d, -d)
    glVertex3d(-d, d, -d)
    glVertex3d(-d, d, d)

    glVertex3d(d, -d, d)
    glVertex3d(d, -d, -d)
    glVertex3d(-d, -d, -d)
    glVertex3d(-d, -d, d)

    glEnd()

def cube_for_skybox():
    glBegin(GL_QUADS)
    glTexCoord2f(0.75, 0.0)
    glVertex3d(-1.0, -1.0, 1.0)
    glTexCoord2f(0.50, 0.0)
    glVertex3d(1.0, -1.0, 1.0)
    glTexCoord2f(0.50, 0.5)
    glVertex3d(1.0, 1.0, 1.0)
    glTexCoord2f(0.75, 0.5)
    glVertex3d(-1.0, 1.0, 1.0)

    glTexCoord2f(0.00, 0.0)
    glVertex3d(-1.0, -1.0, -1.0)
    glTexCoord2f(0.00, 0.5)
    glVertex3d(-1.0, 1.0, -1.0)
    glTexCoord2f(0.25, 0.5)
    glVertex3d(1.0, 1.0, -1.0)
    glTexCoord2f(0.25, 0.0)
    glVertex3d(1.0, -1.0, -1.0)

    glTexCoord2f(0.25, 1.0)
    glVertex3d(-1.0, 1.0, -1.0)
    glTexCoord2f(0.50, 1.0)
    glVertex3d(-1.0, 1.0, 1.0)
    glTexCoord2f(0.50, 0.5)
    glVertex3d(1.0, 1.0, 1.0)
    glTexCoord2f(0.25, 0.5)
    glVertex3d(1.0, 1.0, -1.0)

    glTexCoord2f(0.50, 0.5)
    glVertex3d(-1.0, -1.0, -1.0)
    glTexCoord2f(0.50, 1.0)
    glVertex3d(1.0, -1.0, -1.0)
    glTexCoord2f(0.75, 1.0)
    glVertex3d(1.0, -1.0, 1.0)
    glTexCoord2f(0.75, 0.5)
    glVertex3d(-1.0, -1.0, 1.0)

    glTexCoord2f(0.25, 0.0)
    glVertex3d(1.0, -1.0, -1.0)
    glTexCoord2f(0.25, 0.5)
    glVertex3d(1.0, 1.0, -1.0)
    glTexCoord2f(0.50, 0.5)
    glVertex3d(1.0, 1.0, 1.0)
    glTexCoord2f(0.50, 0.0)
    glVertex3d(1.0, -1.0, 1.0)

    glTexCoord2f(1.00, 0.0)
    glVertex3d(-1.0, -1.0, -1.0)
    glTexCoord2f(0.75, 0.0)
    glVertex3d(-1.0, -1.0, 1.0)
    glTexCoord2f(0.75, 0.5)
    glVertex3d(-1.0, 1.0, 1.0)
    glTexCoord2f(1.00, 0.5)
    glVertex3d(-1.0, 1.0, -1.0)
    glEnd()