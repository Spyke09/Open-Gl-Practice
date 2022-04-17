import math


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(%.2f, %.2f, %.2f)" % (self.x, self.y, self.z)

    def len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def norm(self):
        l = self.len()
        return Vector3(self.x / l, self.y / l, self.z / l) if l else Vector3(0,0,0)

    def xR(self, r):
        return Vector3(self.x * r, self.y * r, self.z * r)

    def plusV(self, v):
        return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)

    def minusV(self, v):
        return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)

    def dotV(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def xV(self, v):
        x = self.y * v.z - self.z * v.y
        y = self.z * v.x - self.x * v.z
        z = self.x * v.y - self.y * v.x
        return Vector3(x, y, z)


class Matrix3x3:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "({},\n {},\n {})".format(self.a, self.b, self.c)

    @staticmethod
    def I():
        return Matrix3x3(Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1))

    def plusM(self, m):
        return Matrix3x3(self.a.plusV(m.a), self.b.plusV(m.b), self.c.plusV(m.c))

    def minusM(self, m):
        return Matrix3x3(self.a.minusV(m.a), self.b.minusV(m.b), self.c.minusV(m.c))

    def transpose(self):
        return Matrix3x3(
            Vector3(self.a.x, self.b.x, self.c.x),
            Vector3(self.a.y, self.b.y, self.c.y),
            Vector3(self.a.z, self.b.z, self.c.z)
        )

    def xM(self, m):
        tr_m = m.transpose()
        a = Vector3(self.a.dotV(tr_m.a), self.a.dotV(tr_m.b), self.a.dotV(tr_m.c))
        b = Vector3(self.b.dotV(tr_m.a), self.b.dotV(tr_m.b), self.b.dotV(tr_m.c))
        c = Vector3(self.c.dotV(tr_m.a), self.c.dotV(tr_m.b), self.c.dotV(tr_m.c))
        return Matrix3x3(a, b, c)

    def xR(self, r):
        return Matrix3x3(self.a.xR(r), self.b.xR(r), self.c.xR(r))

    def xV(self, v):
        return Vector3(self.a.dotV(v), self.b.dotV(v), self.c.dotV(v))

    @staticmethod
    def MRot(v, alpha):
        x_s = Vector3(0, v.z, -v.y)
        y_s = Vector3(-v.z, 0, v.x)
        z_s = Vector3(v.y, -v.x, 0)
        S = Matrix3x3(x_s, y_s, z_s)
        return Matrix3x3.I().plusM(S.xR(math.sin(alpha))).plusM(S.xM(S).xR(1-math.cos(alpha))).xM(Matrix3x3.I())


