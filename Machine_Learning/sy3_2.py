import numpy as np
import math

def f(x):
    return x**3 + (math.e**x)/2.0 + 5.0*x - 6

def loss_fun(x):
    return(f(x))**2

def calcu_grad(x):
    delta=0.0000001
    return(loss_fun(x+delta) - loss_fun(x-delta))/(2.0*delta)

alpha=0.01
maxTimes=100
x=0.0

for i in range(maxTimes):
    x=x-alpha*calcu_grad(x)
    print(str(i)+":"+str(x))
