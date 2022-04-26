# -*- coding: utf-8 -*-
"""
实验四： 平面二分类线性逻辑回归算法的实现
实验目的：
1、实现二分类线性逻辑回归分类器算法。
2、通过代码实现加深对线性逻辑回归分类器算法的理解。
"""

import random
import matplotlib.pyplot as plt
import numpy as np


# ==============================================================================
# 1. 在平面上产生100个点作为实验样本，并根据线x2 = 2*x1 - 30来定标签，线以上标签为1，以下为0.

def f(x_1, x_2):
    '''给平面上的数据点打标签，直线上面的点标签为1，否则为0
    para x: float, x值
    para y: float, y值
    return: int 0-1标签值'''
    yp = 2.0 * x_1 - 30
    if x_2 > yp:
        return 1
    else:
        return 0


samples = []
for i in range(0, 100):
    x_1 = random.uniform(0, 100)
    x_2 = random.uniform(0, 100)
    samples.append([x_1, x_2, f(x_1, x_2)])

x1_1 = []
x1_2 = []
x0_1 = []
x0_2 = []
for x in samples:
    if x[-1] > 0.0:
        x1_1.append(x[0])
        x1_2.append(x[1])
    else:
        x0_1.append(x[0])
        x0_2.append(x[1])
plt.scatter(x1_1, x1_2, c='r', marker='.')
plt.scatter(x0_1, x0_2, c='b', marker='x')
plt.show()


# ==============================================================================
# 2.用梯度下降法求解

# ------------------------------------------------
# 代表虚线的函数
def fw(W, x):
    return (W * x)[0, 0]


# sigmoid函数
def g(z):
    return (1 / (1 + np.exp(-z)))


# 损失函数
def lossValue(W, x, y):
    LW = 0.0
    for i in range(len(y)):
        # ff = fw(W, np.mat(x[:,i]).T)
        hw = g(fw(W, np.mat(x[:, i]).T))
        LW = LW + y[i] * np.log(hw) + (1 - y[i]) * np.log(1 - hw)
    if np.isnan(LW):
        return (np.inf)
    return -1.0 * LW


# 梯度
def gradient(x, y, W):
    n, m = np.shape(x)
    gg = np.mat(np.zeros((n, 1)))
    for j in range(n):
        err = 0.0
        for i in range(m):
            hw = g(fw(W, np.mat(x[:, i]).T))
            err = err + x[j, i] * (hw - y[i])
        gg[j] = err
        # print(gg)
    return gg


# ------------------------------------------------
# 梯度下降法主流程
W = np.mat([0.0, 0.0, 0.0])
samples = np.array(samples)
x = np.c_[np.ones((samples.shape[0], 1)), samples[:, 0:2]]
x = x.T
y = samples[:, -1]
alpha = 0.00001
loss_change = 0.000001
loss = lossValue(W, x, y)
print(loss)

IterNum = 10000
for i in range(IterNum):
    if i < 15000:
        alpha = 0.0001
    elif i < 30000:
        alpha = 0.00005
    elif i < 40000:
        alpha = 0.00001
    else:
        alpha = 0.000005
    W = W - alpha * gradient(x, y, W).T
    newloss = lossValue(W, x, y)

    if i % 1000 == 0:
        print(str(i) + ":: " + str(W[0, 0]) + ' : ' + str(W[0, 1]) + ' : ' + str(W[0, 2]))
        print(newloss)

    if abs(loss - newloss) < loss_change:
        break
    loss = newloss

# ------------------------------------------------
# 用求解得到的系数画出划分虚线
plt.scatter(x1_1, x1_2, c='r', marker='.')
plt.scatter(x0_1, x0_2, c='b', marker='x')
tx_1 = np.linspace(15, 65, 100)
w1 = W[0, 1] / W[0, 2]
w0 = W[0, 0] / W[0, 2]
tx_2 = - w1 * tx_1 - w0
plt.plot(tx_1, tx_2, color="black", linewidth=2, linestyle="--")
plt.show()
