import numpy as np
import math
import time

# 半径
r = 3
# 圆心
a, b = (7.0, 0.0)

# 光源
# ax.scatter(0, 30, -10)

# 画初始圆
degree_rotate = math.pi/8
theta = np.arange(0, math.pi*2, degree_rotate)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z = 0.0


coodX = np.array([])
coodY = np.array([])
coodZ = np.array([])


def rotate_x(x, y, z, degree):
    return [x, y*math.cos(degree)-z*math.sin(degree), y * math.sin(degree) + z * math.cos(degree)]


def rotate_y(x, y, z, degree):
    return [z * math.sin(degree) + x * math.cos(degree), y, z * math.cos(degree) - x * math.sin(degree)]


def rotate_z(x, y, z, degree):
    return [x * math.cos(degree) - y * math.sin(degree), x * math.sin(degree) + y * math.cos(degree), z]


def flat(x, y, z):
    newZ = []
    for _ in x:
        newZ.append(20)
    return [x, y, newZ]


offset = -1
def flat_test(x, y, z):
    global offset
    width = 80
    height = 40
    matrix = [[None for i in range(width)] for i in range(height)]

    # print(min(x[np.argmin(x)],y[np.argmin(y)]))
    if offset < 0:
        offset = abs(min(x[np.argmin(x)],y[np.argmin(y)]))
    x = (x+offset)*1.7
    y = (y+offset)*2.5

    for i in range(len(x)):

        tmp_x = round(x[i])
        tmp_y = round(y[i])

        if 0 > tmp_x >= width or 0 > tmp_y >= height:
            continue

        if (matrix[tmp_x][tmp_y] != None and matrix[tmp_x][tmp_y] < z[i]) or matrix[tmp_x][tmp_y] == None:
            # dot_product = x[i]*0+y[i]*30-z[i]*10
            # if dot_product < 0:
            #     print(dot_product)
            #     continue
            matrix[tmp_x][tmp_y] = z[i]

    print_matrix(matrix)


def print_matrix(matrix):
    str = ''
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] != None:
                str += "."
            else:
                str += " "
        str += "\n"
    print(str)


degree_rotate = math.pi/18

for i in np.arange(0, math.pi*2, degree_rotate):

    cood = rotate_y(x, y, z, degree=i)
    orgin_cood = rotate_y(a, b, 0, degree=i)
    coodX = np.hstack((coodX, cood[0]))
    coodY = np.hstack((coodY, cood[1]))
    coodZ = np.hstack((coodZ, cood[2]))


def drew2():
    degree = math.pi/36
    newCood = rotate_z(coodX, coodY, coodZ, degree=degree)
    while True:
        print("\x1b\x63", end="")
        newCood = rotate_y(newCood[0], newCood[1], newCood[2], degree=degree)
        newCood = rotate_x(newCood[0], newCood[1], newCood[2], degree=degree)
#        newCood = rotate_z(newCood[0], newCood[1], newCood[2], degree=degree)
        flat_test(newCood[0], newCood[1], newCood[2])
        time.sleep(0.1)


def main():
    print("\x1b\x63", end="")
    drew2()


if __name__ == '__main__':
    main()
