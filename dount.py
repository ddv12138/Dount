import numpy as np
import math
import time

# 半径
r = 3
# 圆心
a, b = (7.0, 0.0)

# 光源
light = [-2,-2,-4]

# 画初始圆
rotate_half_round = 16
degree_rotate = math.pi/rotate_half_round
theta = np.arange(0, math.pi*2, degree_rotate)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z = 0.0

def rotate_x(x, y, z, degree):
    return [x, y*math.cos(degree)-z*math.sin(degree), y * math.sin(degree) + z * math.cos(degree)]


def rotate_y(x, y, z, degree):
    return [z * math.sin(degree) + x * math.cos(degree), y, z * math.cos(degree) - x * math.sin(degree)]


def rotate_z(x, y, z, degree):
    return [x * math.cos(degree) - y * math.sin(degree), x * math.sin(degree) + y * math.cos(degree), z]

degree_rotate = math.pi/44

coodX = np.array([])
coodY = np.array([])
coodZ = np.array([])

oCoodX = np.array([])
oCoodY = np.array([])
oCoodZ = np.array([])

for i in np.arange(0, math.pi*2, degree_rotate):

    cood = rotate_y(x, y, z, degree=i)
    coodX = np.hstack((coodX, cood[0]))
    coodY = np.hstack((coodY, cood[1]))
    coodZ = np.hstack((coodZ, cood[2]))

    oCood = rotate_y(a, b, 0, degree=i)
    oCoodX = np.hstack((oCoodX, oCood[0]))
    oCoodY = np.hstack((oCoodY, oCood[1]))
    oCoodZ = np.hstack((oCoodZ, oCood[2]))

offset = -1
def flat_test(x, y, z,oCood):
    global offset
    width = 80
    height = 40
    matrix = [[None for i in range(width)] for i in range(height)]

    if offset < 0:
        offset = abs(min(x[np.argmin(x)],y[np.argmin(y)]))

    for i in range(len(x)):

        tmp_x = round((x[i]+offset+3)*1.7)
        tmp_y = round((y[i]+offset+1)*3.5)

        if 0 > tmp_x >= width or 0 > tmp_y >= height:
            continue

        tmp = int(i/(2*rotate_half_round))
        currCircleCenter = [oCood[0][tmp],oCood[1][tmp],oCood[2][tmp]]
        surfaceNormal = [x[i]-currCircleCenter[0],y[i]-currCircleCenter[1],z[i]-currCircleCenter[2]]
        dotProduct = np.dot(light,surfaceNormal)

        if (matrix[tmp_x][tmp_y] != None and matrix[tmp_x][tmp_y] > z[i]) or matrix[tmp_x][tmp_y] == None:
            if dotProduct>=0:
                matrix[tmp_x][tmp_y] = dotProduct

    print_matrix(matrix)


def print_matrix(matrix):
    str = ''
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] != None:
                # str += "."
                index = round(matrix[x][y])
                if index>11:
                    index = 11
                # print(index)
                str += ".,-~:;=!*#$@"[index]
            else:
                str += " "
        str += "\n"
    print(str)


def drew():
    degree = math.pi/36
    newCood = rotate_z(coodX, coodY, coodZ, degree=degree)
    newOCood = rotate_z(oCoodX, oCoodY, oCoodZ, degree=degree)
    while True:
        print("\x1b\x63", end="")
        newCood = rotate_y(newCood[0], newCood[1], newCood[2], degree=degree)
        newCood = rotate_x(newCood[0], newCood[1], newCood[2], degree=degree)
        newCood = rotate_z(newCood[0], newCood[1], newCood[2], degree=degree)

        newOCood = rotate_y(newOCood[0], newOCood[1], newOCood[2], degree=degree)
        newOCood = rotate_x(newOCood[0], newOCood[1], newOCood[2], degree=degree)
        newOCood = rotate_z(newOCood[0], newOCood[1], newOCood[2], degree=degree)
        flat_test(newCood[0], newCood[1], newCood[2],newOCood)
        time.sleep(0.1)


def main():
    print("\x1b\x63", end="")
    drew()


if __name__ == '__main__':
    main()
