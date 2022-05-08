import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def __str__(self):
        return "({0:.2f}, {1:.2f})".format(self.x, self.y)


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.b >= 0 and self.c >= 0:
            return "{0:.2f}x + {1:.2f}y + {2:.2f} = 0".format(self.a, self.b, self.c)
        if self.b <= 0 and self.c >= 0:
            return "{0:.2f}x - {1:.2f}y + {2:.2f} = 0".format(self.a, -self.b, self.c)
        if self.b >= 0 and self.c <= 0:
            return "{0:.2f}x + {1:.2f}y - {2:.2f} = 0".format(self.a, self.b, -self.c)
        if self.b <= 0 and self.c <= 0:
            return "{0:.2f}x - {1:.2f}y - {2:.2f} = 0".format(self.a, -self.b, -self.c)

    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1 - y2, x2 - x1, x1 * y2 - x2 * y1)

    def distanceToZero(self):
        return abs(self.c) / math.sqrt(self.a ** 2 + self.b ** 2)

    def distanceToPoint(self, p):
        return abs(self.a * p.x + self.b * p.y + self.c) / math.sqrt(self.a ** 2 + self.b ** 2)

    def isParallel(self, l):
        eps = 0.001
        return abs(self.a * l.b - self.b * l.a) < eps

    def intersection(self, l):
        eps = 0.001
        det = self.a * l.b - self.b * l.a
        x1 = (-self.c * l.b + self.b * l.c)
        x2 = (-self.a * l.c + self.c * l.a)
        if abs(det) < eps:
            return None
        return Point(x1 / det, x2 / det)

    def nearPoint(self, p):
        eps = 0.00001
        if abs(self.b) < eps:
            return Point(-self.c / self.a, p.y)
        f = (lambda x: -(x * self.a + self.c) / self.b)
        left = -1e10
        right = 1e10
        while 1:
            l1 = Line.fromCoord(left, f(left), p.x, p.y)
            l2 = Line.fromCoord(right, f(right), p.x, p.y)
            s1 = l1.a * self.a + l1.b * self.b
            s2 = l2.a * self.a + l2.b * self.b
            if abs(s1) < eps:
                return Point(left, f(left))
            left, right = (left, (left + right) / 2) if abs(s1) < abs(s2) else ((left + right) / 2, right)

    def oneSide(self, point1, point2):
        eps = 0.001
        p1 = self.a * point1.x + self.b * point1.y + self.c
        p2 = self.a * point2.x + self.b * point2.y + self.c
        if abs(p1) < eps or abs(p2) < eps:
            return True
        if p1 * p2 >= 0:
            return True
        return False

    def oneSide1(self, point1, point2):
        p1 = self.a * point1.x + self.b * point1.y + self.c
        p2 = self.a * point2.x + self.b * point2.y + self.c
        print(self.a, self.b, self.c)
        if p1 * p2 >= 0:
            return True
        else:
            return False

    def normalize(self):
        eps = 0.001
        if not abs(self.c) < eps:
            self.a /= self.c
            self.b /= self.c
            self.c = 1
        elif not abs(self.a) < eps:
            self.b /= self.a
            self.a = 1
        else:
            self.b = 1
        if abs(self.a) < eps:
            self.a = 0
        if abs(self.b) < eps:
            self.b = 0
        if abs(self.c) < eps:
            self.c = 0

    def perpendicularLine(self, p):
        eps = 0.001
        q = self.nearPoint(p)
        if abs(q.x - p.x) + abs(q.y - p.y) < eps:
            t = Line(self.a, self.b, self.c + 10)
            q = t.nearPoint(p)
        l = Line.fromCoord(p.x, p.y, q.x, q.y)
        return l

    def parallelLine(self, p):
        l1 = self.perpendicularLine(p)
        return l1.perpendicularLine(p)

    def projectionLength(self, p1, p2):
        p3 = self.nearPoint(p1)
        p4 = self.nearPoint(p2)
        return p3.distanceTo(p4)

    def middlePoint(self, p):
        q = self.nearPoint(p)
        return Point((p.x + q.x) / 2, (p.y + q.y) / 2)

    def symmetricPoint(self, p):
        q = self.nearPoint(p)
        return Point(-p.x + 2 * q.x, -p.y + 2 * q.y)

    def insideTreug(self, p):
        self.normalize()
        f = abs(p.x) <= abs(1 / self.a) and p.y <= abs(1 / self.b)
        if self.a > 0 and self.b > 0:
            return p.x <= 0 and p.y <= 0 and f
        if self.a < 0 and self.b > 0:
            return p.x >= 0 and p.y <= 0 and f
        if self.a > 0 and self.b < 0:
            return p.x <= 0 and p.y >= 0 and f
        if self.a < 0 and self.b < 0:
            return p.x >= 0 and p.y >= 0 and f
        return False

    def rotatedLine(self, p):
        p1 = self.nearPoint(p)
        p2 = Point((p1.y - p.y) + p.x, -(p1.x - p.x) + p.y)
        return self.fromCoord(p.x, p.y, p2.x, p2.y).perpendicularLine(p2)

    def bisectrix(self, l):
        eps = 0.001
        if abs(l.a * self.a + l.b * self.b) < eps:
            return None
        if l.isParallel(self):
            if abs(self.b) < eps:
                return Line(1, 0, (self.c / self.b + l.c / l.c) / 2)
            else:
                return Line(self.a/self.b, 1, (self.c / self.b + l.c / l.c) / 2)
        fi1 = math.pi / 2 if abs(self.b) < eps else math.atan(-self.a / self.b)
        fi2 = math.pi / 2 if abs(l.b) < eps else math.atan(-l.a / l.b)
        fi3 = (fi1 + fi2) / 2
        p = self.intersection(l)
        px, py = p.x, p.y
        a = math.sin(fi3)
        b = -math.cos(fi3)
        c = -(px * a + py * b)
        return Line(a, b, c)


# l1 = Line.fromCoord(1, 1, -2, -2)
# l2 = Line.fromCoord(0, 1, 1, 0)
# ans = l1.bisectrix(l2)
# print(ans)
