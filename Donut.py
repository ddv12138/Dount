from matplotlib import pyplot as plt

import numpy as np
import math
import os
import time

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x轴')
ax.set_ylabel('y轴')
ax.set_zlabel('z轴')

# x轴
distance = 20
ax.plot([-distance, distance], [0, 0], [0, 0])
# y轴
ax.plot([0, 0], [-distance, distance], [0, 0])
# z轴
ax.plot([0, 0], [0, 0], [-distance, distance])

plt.axis()

# 半径
r = 3
# 圆心
a, b = (8.0, 8.0)
# 画出圆心点
#ax.scatter(a, b, 0.0)

# 光源
ax.scatter(0, 30, -10)

# 画初始圆
degree_rotate = math.pi/10
theta = np.arange(0, math.pi*2, degree_rotate)
#theta = np.arange(0.0, 2 * np.pi, 0.5)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
z = 0.0
# ax.scatter(x, y, 0, c='r')


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


def flat_test(x, y, z):
    size = 80
    matrix = [[None for i in range(size)] for i in range(size)]

    x = (x+20)*2
    y = (y+15)*2
    #x = x * 2;y = y * 2

    for i in range(len(x)):

        tmp_x = round(x[i])
        tmp_y = round(y[i])

        if tmp_x >= size or tmp_y >= size:
            continue

        # if (matrix[tmp_x][tmp_y] != None and matrix[tmp_x][tmp_y] < z[tmp_x]) or matrix[tmp_x][tmp_y] == None:
        if (matrix[tmp_x][tmp_y] != None and matrix[tmp_x][tmp_y] < z[i]) or matrix[tmp_x][tmp_y] == None:
            # print((tmp_x,tmp_y))
            matrix[tmp_x][tmp_y] = z[i]

    print_matrix(matrix)


def print_matrix(matrix):
    str = ''
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] != None:
                str += ". "
            else:
                str += "  "
        str += "\n"
    print(str)


degree_rotate = math.pi/16

for i in np.arange(0, math.pi*2, degree_rotate):

    cood = rotate_y(x, y, z, degree=i)
    orgin_cood = rotate_y(a, b, 0, degree=i)
    coodX = np.hstack((coodX, cood[0]))
    coodY = np.hstack((coodY, cood[1]))
    coodZ = np.hstack((coodZ, cood[2]))


def test():
    for i in range(100):
        os.system("cls")
        flat_ascii(i)
        time.sleep(0.1)


def drew():
    ax.scatter(coodX, coodY, coodZ, c='g')
    newCood = rotate_z(coodX, coodY, coodZ, degree=math.pi/6)
    ax.scatter(newCood[0], newCood[1], newCood[2], c='g')
    plt.show()


def drew2():
    degree = math.pi/36
    newCood = rotate_z(coodX, coodY, coodZ, degree=degree)
    while True:
        print("\x1b\x63", end="")
        # os.system("cls")
        newCood = rotate_x(newCood[0], newCood[1], newCood[2], degree=degree)
        newCood = rotate_y(newCood[0], newCood[1], newCood[2], degree=degree)
        flat_test(newCood[0], newCood[1], newCood[2])
        time.sleep(0.1)


def main():
    # os.system("clear")
    print("\x1b\x63", end="")
    # drew()
    drew2()


if __name__ == '__main__':
    main()
