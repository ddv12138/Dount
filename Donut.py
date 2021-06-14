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
r = 2.0
# 圆心
a, b = (10.0, 10.0)
# 画出圆心点
#ax.scatter(a, b, 0.0)

# 光源
ax.scatter(0, 30, -10)

# 画初始圆
theta = np.arange(0.0, 2 * np.pi, 1.0)
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
    matrix = [[-1 for i in range(52)] for i in range(51)]
    x = x+25
    y = y+25
    for i in range(len(x)):
        for j in range(len(y)):
            tmp_x = round(x[i])
            tmp_y = round(x[j])
            if (matrix[tmp_x][tmp_y] > 0 and matrix[tmp_x][tmp_y] > z[tmp_x]) or matrix[tmp_x][tmp_y] < 0:
                matrix[tmp_x][tmp_y] = z[tmp_x]
    print_matrix(matrix)

def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y]>0:
                print(".",end=' ')
            else:
                print(" ",end=' ')
        print()

def flat_ascii(num):
    newX = [" "]*51
    newY = [" "]*51
    newZ = [" "]*51

    for i in range(len(newX)):
        for j in range(len(newY)):
            if i == num and j == num:
                print("*  ", end='')
            else:
                print(".  ", end='')
        print()


for i in range(0, 12):
    cood = rotate_y(x, y, z, degree=math.pi / 6*i)
    orgin_cood = rotate_y(a, b, 0, degree=math.pi / 6*i)
    coodX = np.hstack((coodX, cood[0]))
    coodY = np.hstack((coodY, cood[1]))
    coodZ = np.hstack((coodZ, cood[2]))


def test():
    for i in range(100):
        os.system("cls")
        flat_ascii(i)
        time.sleep(0.1)


def main():
    os.system("cls")
    #ax.scatter(newCood[0], newCood[1], newCood[2], c='g')
    # newCood = flat(newCood[0], newCood[1], newCood[2])
    # ax.scatter(newCood[0], newCood[1], newCood[2], c='r')
    # plt.show()
    for _ in range(10):
        os.system("cls")
        newCood = rotate_z(coodX, coodY, coodZ, degree=math.pi/6)
        newCood = rotate_x(newCood[0], newCood[1], newCood[2], degree=math.pi/3)
        flat_test(newCood[0], newCood[1], newCood[2])
        time.sleep(0.5)
    # test()


if __name__ == '__main__':
    main()
