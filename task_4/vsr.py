from vector_and_matrix.vector import Vector3


def GetZ(x, y, H):
    ix = int(x)
    iy = int(y)
    fx = x - ix
    fy = y - iy
    if (ix + iy) % 2 == 0:
        if fx > fy:
            v1 = Vector3(ix, iy + 1, H[ix][iy + 1])
            v2 = Vector3(1, 0, H[ix + 1][iy + 1] - H[ix][iy + 1])
            v3 = Vector3(0, -1, H[ix][iy] - H[ix][iy + 1])
        else:
            v1 = Vector3(ix + 1, iy, H[ix + 1][iy])
            v2 = Vector3(0, 1, H[ix + 1][iy + 1] - H[ix + 1][iy])
            v3 = Vector3(-1, 0, H[ix][iy] - H[ix + 1][iy])
    else:
        if fy < 1 - fx:
            v1 = Vector3(ix, iy, H[ix][iy])
            v2 = Vector3(0, 1, H[ix][iy + 1] - H[ix][iy])
            v3 = Vector3(1, 0, H[ix + 1][iy] - H[ix][iy])
        else:
            v1 = Vector3(ix + 1, iy + 1, H[ix + 1][iy + 1])
            v2 = Vector3(-1, 0, H[ix][iy + 1] - H[ix + 1][iy + 1])
            v3 = Vector3(0, -1, H[ix + 1][iy] - H[ix + 1][iy + 1])

    r1 = v2.xV(v3)
    return -(r1.x * x + r1.y * y - r1.dotV(v1)) / r1.z
