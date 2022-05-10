# -*- coding: utf-8 -*-

#==============================================================================
# 实验目的：了解并掌握线性回归的原理，编程实现简单线性回归问题。
#### 梯度下降法计算简单线性回归的例子

import numpy as np

print('*'*100)


def gradient(x, y, w):
    '''计算一阶导函数的值
    para x: 矩阵, 样本集
    para y: 矩阵, 标签
    para w: 矩阵, 线性回归模型的参数
    return: 矩阵, 一阶导数值
    '''
    m, n = np.shape(x)
    g = np.mat(np.zeros((n, 1)))
    for i in range(m):
        err = y[i, 0] - x[i, ] * w
        for j in range(n):
            g[j, ] -= err * x[i, j]
    return g    


def lossValue(x, y, w):
    '''计算损失函数
    para x: 矩阵, 样本集
    para y: 矩阵, 标签
    para w: 矩阵, 线性回归模型的参数
    return: 损失函数值'''
    k = y - x*w
    return k.T * k / 2


temperatures = [15, 20, 25, 30, 35, 40]
flowers = [136, 140, 155, 160, 157, 175]
X = (np.mat([[1,1,1,1,1,1], temperatures])).T
y = (np.mat(flowers)).T

W = (np.mat([0.0,0.0])).T
print(W)
#alpha = 0.0005 # 步长太大，来回振荡，无法收敛
alpha = 0.00025
loss_change = 0.000001
loss = lossValue(X, y, W)
for i in range(30000):
    W = W - alpha * gradient(X, y, W)
    newloss = lossValue(X, y, W)
    print(str(i)+":"+str(W[0])+':'+str(W[1]))
    print(newloss)
    if abs(loss - newloss) < loss_change:
        break
    loss = newloss

new_tempera = [18, 22, 33]
new_tempera = (np.mat([[1,1,1], new_tempera])).T
pro_num = new_tempera * W
print(pro_num)

